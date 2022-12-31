# Write your code below. See the Instructions in the tab to the right
cost = 20
desire = int(input('How many books do you want to buy? '))
reality = int(input('How much money do you have? '))
check = cost * desire
truth = abs(reality - check)
if(reality >= check):
    # You have Enough Money, Go for it.
    print('You have enough money, go for it!')
else:
    # You Don't Have Enough Money, You need {truth} amount.
    print(f'You need ${truth} more to buy that number of books')