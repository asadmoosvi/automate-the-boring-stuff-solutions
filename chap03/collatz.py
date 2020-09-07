import sys

def main() -> int:
    while True:
        try:
            number = int(input('Enter a starting number for the collatz sequence: '))
            break
        except ValueError:
            print('[error] Invalid input, no number recieved. Please try again.')

    print_collatz_seq(number)
    return 0

def collatz(number: int) -> None:
    if number % 2:
        return number * 3 + 1
    else:
        return number // 2

def print_collatz_seq(number: int) -> None:
    print(f'Starting number: {number}')
    while number != 1:
        number = collatz(number)
        print(f'New number: {number}')
    print('End of sequence.')

if __name__ == '__main__':
    sys.exit(main())
