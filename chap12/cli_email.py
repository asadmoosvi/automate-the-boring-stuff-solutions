'''
Uses ProtonMail to Send an Email.
'''

from typing import Optional, Sequence
import sys
import argparse
import yaml
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description='Send an Email to Someone')
    parser.add_argument('-t', '--to', help="Receiver's email address")
    parser.add_argument('-s', '--subject', help='Subject of the email',
                        default='default subject')
    parser.add_argument('-b', '--body',  help='Body of the email',
                        default='default body')
    parser.add_argument('-f', '--file', type=argparse.FileType('r'),
                         help='File content to use as body')
    argv = argv if argv is not None else sys.argv[1:]
    args = parser.parse_args(argv)

    if not os.path.exists('auth.yml'):
        print('\nCannot send email without sender information.')
        print('Please make sure the `auth.yml` file exists in the current directory.')
        print('Expecting yaml format:')
        print('  username: your protonmail username')
        print('  password: your protonmail password')
        sys.exit(1)

    with open('auth.yml') as f:
        auth_yml = yaml.safe_load(f.read())

    bot_email = auth_yml['username']
    bot_password = auth_yml['password']

    if args.to:
        if args.file:
            args.body =  args.file.read()
            args.file.close()
        send_mail(bot_email, bot_password, args.to, args.subject, args.body)
    else:
        parser.print_help()
        return 1

    return 0


def send_mail(
    bot_email: str,
    bot_password: str,
    to_email: str,
    subject: str,
    body: str
) -> None:
    print("\nSending email...\n")
    print(
        f'From   : {bot_email}\n'
        f'To     : {to_email}\n'
        f'Subject: {subject}\n'
        f'\n{body}'
    )

    browser = webdriver.Chrome()
    browser.get('https://mail.protonmail.com')
    sleep(3)

    # login
    username_box = browser.find_element_by_id('username')
    username_box.send_keys(bot_email)
    password_box = browser.find_element_by_id('password')
    password_box.send_keys(bot_password)
    password_box.submit()
    sleep(3)

    # compose mail and send
    compose_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#pm_sidebar > button')
        )
    )
    compose_button.click()

    to_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/form[1]/div/div[2]/div[2]/form/div/div/div/input')
        )
    )
    to_field.send_keys(to_email)
    subject_field = browser.find_element_by_xpath(
        '/html/body/div[2]/form[1]/div/div[2]/div[5]/input'
    )
    subject_field.send_keys(subject)

    email_content_frame = browser.find_element_by_class_name('squireIframe')
    browser.switch_to.frame(email_content_frame)
    body_field = browser.find_element_by_tag_name('body')
    body_field.send_keys(body)

    browser.switch_to.default_content()
    submit_button = browser.find_element_by_xpath(
        '//*[@id="uid1"]/footer/div/button[3]'
    )
    submit_button.click()
    sleep(3)

    browser.quit()

    print('\nEmail successfully sent!')


if __name__ == '__main__':
    exit(main())
