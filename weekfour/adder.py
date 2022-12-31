10-20# Find the sum of just the odd numbers in this list
numbers = [62, 60, 53, 53, 33, 3, 25, 61, 36, 1, 69, 55, 56, 39, 32, 76, 20, 62, 47]

# Sum Odd Numbers
sum = 0
for i in numbers:
    if i % 2 != 0:
        sum += i
print(sum)