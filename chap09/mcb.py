# multiclipboard:
#   a program to store different clipboard contents
#   by keywords in a shelf file

import sys, shelve, pyperclip
from typing import Optional, Sequence

shelf_filename = 'mcb.dat'

def print_usage() -> None:
    print(f'Usage: {sys.argv[0]} <keyword> | list | save <keyword> | delete [<keyword>]')
    print(
        '\nArguments:\n'
        '\t<keyword> fetches the value of that key from the db\n'
        '\tlist: lists all the keys and their values\n'
        '\tsave: save clipboard contents in the the key provided by <keyword>\n'
        '\tdelete: delete entire database or delete a keyword'
    )

def main(argv: Optional[Sequence[str]] = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    shelf_file = shelve.open(shelf_filename)
    if len(argv) == 1:
        if argv[0].lower() == 'list':
            print('Items'.center(80, '-'))
            print('Key'.ljust(40) + 'value'.ljust(40))
            print('---'.ljust(40) + '-----'.ljust(40))
            if len(shelf_file) == 0:
                print()
                print('(EMPTY)'.center(80))
            else:
                for key, val in shelf_file.items():
                    print(f'{key}'.ljust(40) + f'{val}'.ljust(40))
        elif argv[0].lower() == 'delete':
            print('==> deleting entire database')
            shelf_file.clear()
        elif argv[0] in shelf_file:
            print('copying the following key to clipboard...')
            print(f'===> {argv[0]}: {shelf_file[argv[0]]}')
            pyperclip.copy(shelf_file[argv[0]])
        else:
            print(f'==> key `{argv[0]}` does not exist')
            return 1
    elif len(argv) == 2 and argv[0].lower() == 'save':
        print(f'==> Saving data to key `{argv[1]}`')
        shelf_file[argv[1]] = pyperclip.paste()
    elif len(argv) == 2 and argv[0].lower() == 'delete':
        if argv[1] not in shelf_file:
            print(f'==> key `{argv[1]}` does not exist')
            return 1
        else:
            print(f'==> deleting key `{argv[1]}` from database')
            del shelf_file[argv[1]]
    else:
        print_usage()
        return 1

    shelf_file.close()
    return 0

if __name__ == '__main__':
    exit(main())
