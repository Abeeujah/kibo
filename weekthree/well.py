# Prompt User for Input and handle errors
user_input = input('Enter your number: ')
if user_input.isdecimal():
    user_input = int(user_input)
else:
    print(f'Error, your input {user_input} is not a number')

# Check it's multiple
if user_input % 3 == 0 and user_input % 5 == 0:
    print(f'{user_input} is divisible by 3 and 5')
elif user_input % 3 == 0:
    print(f'{user_input} is divisible by 3')
elif user_input % 5 == 0:
    print(f'{user_input} is divisible by 5')
else:
    print(f'Your number is {user_input}')