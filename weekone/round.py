# Get two numbers as input from the user
# Convert the inputs to floats
float_one = float(input('Enter your first number: '))
float_two = float(input('Enter your second number: '))

# Divide one number by the other
divisor = (float_one / float_two)

# Print the result, rounded to 3 digits using f-strings
rounded_float = f'{divisor:.3f}'
print(rounded_float)