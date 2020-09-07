import sys
import time

def main() -> int:
    if len(sys.argv) != 3:
        print(f'Usage: python {sys.argv[0]} indent n\n')
        print('arguments meaning:')
        print('    ~> indent: indentation level of a line')
        print('    ~> n: time between each printing of a line in seconds')
        sys.exit(1)

    indent = int(sys.argv[1])
    n = float(sys.argv[2])
    zigzag(indent, n)
    return 0

def zigzag(indent: int, n: float) -> None:
    try:
        while True:
            for i in range (indent, -1, -1):
                print_line('*', 10, i)
                time.sleep(n)
                # make a beep when indentation is 0 (simulate a bounce effect)
                if i == 0:
                    print('\a', end='')

            for i in range(0, indent + 1):
                print_line('*', 10, i)
                time.sleep(n)
                # make a beep when indentation is max (simulate a bounce effect)
                if i == indent - 1:
                    print('\a', end='')
    except KeyboardInterrupt:
        print('Goodbye!')


def print_line(char, char_count, indent) -> None:
    for i in range(indent):
        print(' ', end='')
    print(char * char_count)

if __name__ == '__main__':
    sys.exit(main())
