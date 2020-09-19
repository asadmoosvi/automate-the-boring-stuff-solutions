import re, sys

def main() -> int:
    text = '|**<>HELLO WORLD<>>>*|||'
    stripped_text = regex_strip(text, '|*<>')

    print(f'text before: {text!r}')
    print(f'text stripped: {stripped_text!r}')

    return 0

def regex_strip(s: str, chars: str = None) -> str:
    if chars:
        char_class = '[' + re.escape(chars) + ']'
    else:
        char_class = '\\s'

    regex = re.compile(f'^{char_class}+|{char_class}+$')
    print(f'regex: {regex}')
    return regex.sub('', s)

if __name__ == '__main__':
    sys.exit(main())
