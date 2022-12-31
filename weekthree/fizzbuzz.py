# See Instructions tab

# Print numbers 1 to 100
i = 1
while i <= 100:
    if ((i % 3 == 0) and (i % 5 == 0)):
        print(f'{i} is a multiple of 3 and 5')
    elif(i % 3 == 0):
        # For multiples of 3, print "X is a multiple of 3"
        print(f'{i} is a multiple of 3')
    elif(i % 5 == 0):
        # For multiples of 5, print "X is a multiple of 5"
        print(f'{i} is a multiple of 5')
    else:
        print(i)
    i += 1
