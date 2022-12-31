# Follow the instructions in the tab to the right
# Write your code below

i = 0
words = []
# print('Enter a series of words and get the longest word')
while i < 5:
    word = input('Enter a word: ')
    words.append(word)
    i = i + 1

# Get the longest word
track = 0
longest = ''
for word in words:
    if len(word) > track:
        track = len(word)
        longest = word
print(longest)
        