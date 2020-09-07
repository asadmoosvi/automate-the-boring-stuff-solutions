# this is a gues the number game
import random

secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

for guesses_taken in range(1, 7):
    guess = int(input('Take a guess: '))
    if guess > secret_number:
        print('Your guess is too high.')
    elif guess < secret_number:
        print('Your guess it too low.')
    else:
        break

if guess == secret_number:
    print(f'Good job! You guessed my number in {guesses_taken} guesses!')
else:
    print(f'Nope. The number I was thinking of was {secret_number}.')
