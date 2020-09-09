import sys

def main() -> int:
    spam = ['apples', 'bananas', 'tofu', 'cats']
    sep = ','
    print(f'spam: {list_to_string(spam, sep)}')
    print('\nRunning tests...')
    test()
    return 0

def test() -> None:
    test_mixed = [1, int, 'foo', 'bar', 4.2]
    test_single = ['single']
    test_empty = []
    sep = ','
    print('test_mixed:', list_to_string(test_mixed, sep))
    print('test_single:', list_to_string(test_single, sep))
    if not list_to_string(test_empty, ','):
        print('test_empty:', 'test_empty is an empty list')

def list_to_string(l: list, sep: str) -> str:
    list_s = ''
    if len(l) == 1:
        list_s += str(l[0])
        return list_s

    for x in range(len(l)):
        list_s += str(l[x])
        if x != len(l) - 2 and x != len(l) -1:
            list_s += sep + ' '
        elif x == len(l) - 2:
            list_s += ' and '

    return list_s

if __name__ == '__main__':
    sys.exit(main())
