# Write your solution below
# Follow the instructions in the tab to the right

# Use this exchange rate
NAIRA_PER_DOLLAR = 410.59 # exchange rate as of Nov 10 2021

# Enter USD Value
usd = float(input('Enter USD Value: '))

# Naira Equivalent
naira = usd * NAIRA_PER_DOLLAR

# Round to 2 decimal place
naira = f'{naira:.2f} NGN'
print(naira)