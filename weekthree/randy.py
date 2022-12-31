# See the Instructions tab
from random import randint

# Set secret number
secret = randint(0, 99)
print("I'm thinking of a number between 1 and 99")

# Start Game
game_on = True
while game_on:
    # Ask the user to guess
    guess = input('Enter your guess, between 1 to 99: ')
    if guess.isnumeric():
        guess = int(guess)
    else:
        guess = input('Guess must be a number, between 1 to 99: ')
        if guess.isdecimal():
            guess = int(guess)
        else:
            print('Have a Nice day')
            break

    # Check to see if the guess is <, >, or = secret number
    if guess > secret:
        print('Guess is too high, try again')
    elif guess < secret:
        print('Guess is too low, try again')
    elif guess == secret:
        # Print the right message
        print('You guessed right')
        game_on = False
