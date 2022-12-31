# Find the sum of the even numbers from 10 to 100 (including 10 and 100)
sum = 0
for i in range(0, 101):
    if i % 2 == 0:
        sum += i
print(sum)