# Practice writing for loops using range

# print the numbers from 4 to 14
for number in range(4, 15):
    print(number)

# print the numbers from -10 to 10
for number in range(-10, 11):
    print(number)

# print the numbers from 1 to 20, counting by 2s
for number in range(1, 21, 2):
    print(number)

# print the numbers from 1000 to 500, counting backwards by 100s
for number in reversed(range(500, 1100, 100)):
    print(number)

# for number in reversed(range(1000, 400, -100)):
#     print(number)