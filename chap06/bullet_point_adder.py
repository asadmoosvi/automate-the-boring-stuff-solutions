#!/usr/bin/env python3
import sys, pyperclip

def main() -> int:
    text = pyperclip.paste().strip()
    lines = text.split('\n')
    lines = ['* ' + line for line in lines]
    pyperclip.copy('\n'.join(lines))
    print('    -> Prepended an asterisk before each line in the clipboard.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
