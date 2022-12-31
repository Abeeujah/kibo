# Original instructions: Print the sum of the odd numbers between 10 and 25
# Add print statements to debug the code
total = 0
for i in range(10,25,2):
	print(total)
	total + i
	print(total)
print(total)


# What is wrong with the code? (answer in a comment)
# the expression in the loop is not being reassigned to total
# 
# 