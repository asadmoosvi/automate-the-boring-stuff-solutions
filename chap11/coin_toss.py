import random

guess = ''
while guess not in ('heads', 'tails'):
    guess = input('Guess the coin toss! Enter heads or tails: ')

toss = random.choice(['heads', 'tails'])
if toss == guess:
    print('You got it!')
else:
    guess = input('Nope! Guess again (heads or tails): ')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

