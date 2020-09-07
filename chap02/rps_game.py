# rock, paper, scissors game

import random

def print_stats(wins: int, losses: int, ties: int) -> None:
    print(f'{wins} wins, {losses} losses, {ties} ties.')

def get_move(move: str) -> str:
    if move == 'p':
        return 'PAPER'
    elif move == 's':
        return 'SCISSORS'
    elif move == 'r':
        return 'ROCK'
    else:
        return ''

def move_is_valid(move: str) -> bool:
    return move == 'p' or \
           move == 'r' or \
           move == 's'

def get_winner(computer_move: str, player_move: str) -> str:
    if computer_move == player_move:
        return 'tie'

    if computer_move == 'r' and player_move == 'p':
        return 'player'
    elif computer_move == 'r' and player_move == 's':
        return 'computer'

    if computer_move == 'p' and player_move == 'r':
        return 'computer'
    elif computer_move == 'p' and player_move == 's':
        return 'player'

    if computer_move == 's' and player_move == 'p':
        return 'computer'
    elif computer_move == 's' and player_move == 'r':
        return 'player'

wins = 0
losses = 0
ties = 0
move = ''
choices = ['r', 'p', 's']
computer_move = ''
winner = ''

print('ROCK, PAPER, SCISSORS')

while True:
    print_stats(wins, losses, ties)

    move = input('Enter your move r(ock), p(aper), s(scissors, or q(uit): ')
    if move != 'r' and move != 'p' and move != 's' and move != 'q':
        print(f'Invalid value `{move}`, valid values are r, p, s, or q.\n')
        continue

    if move == 'q':
        break

    computer_move = random.choice(choices)
    print(f'{get_move(move)} versus...\n{get_move(computer_move)}')

    winner = get_winner(computer_move, move)
    if winner == 'tie':
        print('It\'s a tie!')
        ties += 1
    elif winner == 'computer':
        print('You lose!')
        losses += 1
    elif winner == 'player':
        print('You win!')
        wins += 1

    print()

print('Goodbye!')
