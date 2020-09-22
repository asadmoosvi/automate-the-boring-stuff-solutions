import time, random
from typing import Optional

def main() -> int:
    total_questions = 10
    correct_questions = 0
    for i in range(total_questions):
        num_a = random.randint(0, 9)
        num_b = random.randint(0, 9)
        correct_answer = num_a * num_b
        answer = get_int(f'Q{i + 1}: What is {num_a} X {num_b}? ',
                         must_equal=correct_answer,
                         limit=3,
                         timeout=8)
        if answer == correct_answer:
            print('Correct answer!')
            correct_questions += 1
        else:
            print('Incorrect answer!')
    print(f'\nYou got {correct_questions} out of {total_questions} correct.')

    return 0

def get_int(
        prompt: str = '',
        must_equal: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None
) -> Optional[int]:
    start_time = time.time()
    attempts = 0
    user_input = None

    while True:
        try:
            user_input = int(input(prompt))
            if not must_equal:
                break
            if user_input == must_equal:
                break
        except ValueError:
            print('Invalid input.')
        attempts += 1
        if limit and attempts == limit:
            print(f'Max limits of {limit} is over.')
            return None
        print('Try again!')

    end_time = time.time()
    if timeout and end_time - start_time > timeout:
        print(f'Timeout of {timeout} seconds was over.')
        return None
    else:
        return user_input

if __name__ == '__main__':
    exit(main())
