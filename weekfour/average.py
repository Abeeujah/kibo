# See the Instructions tab to the right
# Find the average of the numbers in this list
nums = [-34, -13, 28, -34, 17, 43, -11, -25, 16, -35, 129, 30, 120, 10,
        40, -5, 51, 32, 134, 36, 81, 87, 26, 49, 67, 36, 137, 29, 108, 58, 30]

# Find the Average
sum = 0

# Sum All Numbers using a For Loop
for num in nums:
    sum += num

# Get Average by dividing sum with entries
average = sum / len(nums)
print(sum)
print(average)