# Write a program to find the minimum of numbers provided by the user

# Get how many numbers the user will enter
numbers = int(input("How many numbers will you enter? "))
# set some initial variables before the loop starts
i = 0

# Use minimum to keep track of minimum number
minimum = float('inf')

# write the loop
for i in range(numbers):
  # add code to get the integer and store it in a variable x
    x = int(input('Enter a number: '))
  # check whether x is smaller than minimum, and reassign minimum to it if so
    if x < minimum:
        minimum = x

print("The smallest number is:", minimum)