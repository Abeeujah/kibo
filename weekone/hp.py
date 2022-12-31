# Write your AC Load Estimator solution here
width = float(input('Enter Width of the Room: '))
height = float(input('Enter Height of the Room: '))
number_of_people = float(input('Enter Number of People in the Room: '))

# Calculate HorsePower
horsepower = width * height *  0.1 + number_of_people * 0.06

# Print HorsePower
print(horsepower)