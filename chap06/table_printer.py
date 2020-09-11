import sys

def main() -> int:
    table_data = [
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']
    ]

    print_table(table_data)
    return 0

def print_table(table_data: list) -> None:
    '''Takes a list of lists and prints it in a nice format.'''
    col_widths = [0] * 3
    for col in range(len(table_data)):
        col_widths[col] = max(len(table_item) for table_item in table_data[col])

    rows = len(table_data[0])
    cols = len(table_data)
    for row in range(rows):
        for col in range(cols):
            print(table_data[col][row].rjust(col_widths[col]), end=' ')
        print()

if __name__ == '__main__':
    sys.exit(main())
