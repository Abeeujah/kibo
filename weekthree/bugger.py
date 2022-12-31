# Original instructions: Print the sum of the odd numbers between 10 and 25
# Add print statements to debug the code
total = 0
print(total)
for i in range(10, 25, 2):
    print(total)
    total + i
    print(total)
print(total)


# What is wrong with the code? (answer in a comment)
# Total is being added to a number during every iteration
# But the result of Total is not being updated in memory
# It should be updated using the operator + assignment syntax
# total += i
