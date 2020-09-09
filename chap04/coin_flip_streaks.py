import random
import sys

def main() -> int:
    number_of_streaks = 0
    total_experiments = 10000
    print(f'Finding streaks out of {total_experiments} experiments...\n')

    # all experiments
    for experiment_no in range(total_experiments):
        coin_flips = []
        for x in range(100):
            coin_flips.append(random.randint(0, 1))

        last_coin_flip = coin_flips[0]
        consec_count = 1
        has_streak = False
        for y in range(1, 100):
            if coin_flips[y] == last_coin_flip:
                consec_count += 1
            else:
                if consec_count >= 6:
                    has_streak = True
                last_coin_flip = coin_flips[y]
                consec_count = 1

        # last consec count
        if consec_count >= 6:
            has_streak = True

        if has_streak:
            number_of_streaks += 1

    # summary
    print(
        f'Chance of streak of 6 or more consecutive\n'
        f'heads or tails:\n'
        f'\ttotal experiments: {total_experiments}, streaks: {number_of_streaks}\n'
        f'\tpercentage: ({number_of_streaks / total_experiments * 100} %)'
    );
    return 0

if __name__ == '__main__':
   sys.exit(main())
