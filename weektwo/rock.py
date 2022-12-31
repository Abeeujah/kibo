# Write your solution below the starter code
# Follow the instructions in the tab to the right

import random

# Welcome the user to the game
print("Welcome to rock, paper, scissors. Good luck!")
print("Pay Attention To Instructions To Play!")
print("Rock Smashes Scissors!")
print("Paper Covers Rock!")
print("Scissors Cuts Paper!")
print("GoodLuck!")

# Make a choice for the computer player
choices = ['rock', 'paper', 'scissors']
comp_choice = random.choice(choices)
# Get a choice from the user
user_choice = (input("Enter A Choice between Rock, Paper and Scissors To Continue: ")).lower()
# Compare the user and computer choice
# Print the right message, based on the choices
if user_choice in choices:
    if user_choice == comp_choice:
        print(f"It's A Tie, You Chose {user_choice} and Computer Chose {comp_choice}")
    elif user_choice == 'rock':
        if comp_choice == 'scissors':
            print(f"Computer Choice is {comp_choice}, Rock Smashes Scissors, You Win")
        elif comp_choice == 'paper':
            print(f"Computer Choice is {comp_choice}, Paper Covers Rock, You Lose")
    elif user_choice == 'paper':
        if comp_choice == 'rock':
            print(f"Computer Choice is {comp_choice}, Paper Covers Rock, You Win")
        elif comp_choice == 'scissors':
            print(f"Computer Choice is {comp_choice}, Scissors Cuts Paper, You Lose")
    elif user_choice == 'scissors':
        if comp_choice == 'paper':
            print(f"Computer Choice is {comp_choice}, Scissors Cuts Paper, You Win")
        elif comp_choice == 'rock':
            print(f"Computer Choice is {comp_choice}, Rock Smashes Scissors, You Lose")
else:
    print(f"You Have not Entered A Valid Choice, Your Choice should be Between\nRock, Paper and Scissors")
