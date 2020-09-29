from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys


driver = webdriver.Chrome()
driver.get('https://play2048.co/')

body_elem = driver.find_element_by_tag_name('body')
arrow_keys = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]
while True:
    for arrow_key in arrow_keys:
        body_elem.send_keys(arrow_key)
        game_over = driver.find_elements_by_css_selector(
            'body > div.container > div.game-container'
            ' > div.game-message.game-over > p'
        )
        if game_over:
            driver.quit()
            sys.exit()
