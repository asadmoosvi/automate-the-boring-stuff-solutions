import re, sys

def main() -> int:
    user_password = input('Enter a password: ')
    if is_strong_password(user_password):
        print(f'{user_password!r} is a strong password.')
    else:
        print(f'{user_password!r} is a weak password.\nPlease try again.')
    return 0

def is_strong_password(password: str) -> bool:
    len_regex = re.compile(r'.{8}.*')
    uppercase_regex = re.compile(r'[A-Z]+')
    lowercase_regex = re.compile(r'[a-z]+')
    digit_regex = re.compile(r'\d+')

    good_len = len_regex.search(password)
    good_upper = uppercase_regex.search(password)
    good_lower = lowercase_regex.search(password)
    good_digit = digit_regex.search(password)

    print(f'\n:: Has minimum length of 8: {bool(good_len)}')
    print(f':: Contains uppercase letters: {bool(good_upper)}')
    print(f':: Constains lowercase letters: {bool(good_lower)}')
    print(f':: Contains digits: {bool(good_digit)}')
    print()

    if good_len and good_upper and good_lower and good_digit:
        return True
    else:
        return False

if __name__ == '__main__':
    sys.exit(main())
