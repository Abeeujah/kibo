# Follow the instructions in the tab to the right
# Write your mad libs program here
# Import pyttsx3
import pyttsx3

# Can You Be The Ipsum
dummy = input('Enter your thought: ')
industry = input('Enter your thought: ')
standard = input('Enter your thought: ')
unknown = input('Enter your thought: ')
scrambled = input('Enter your thought: ')
survived = input('Enter your thought: ')
electronic = input('Enter your thought: ')
popularised = input('Enter your thought: ')
letraset = input('Enter your thought: ')
recently = input('Enter your thought: ')
pagemaker = input('Enter your thought: ')

# A Lorem Story
story = f"Lorem Ipsum is simply {dummy} text of the printing and typesetting {industry}. Lorem Ipsum has been the industry's {standard} dummy text ever since the 1500s, when an {unknown} printer took a galley of type and {scrambled} it to make a type specimen book. It has {survived} not only five centuries, but also the leap into {electronic} typesetting, remaining essentially unchanged. It was {popularised} in the 1960s with the release of {letraset} sheets containing Lorem Ipsum passages, and more {recently} with desktop publishing software like Aldus {pagemaker} including versions of Lorem Ipsum."

# Listen To My Story
# Using pyttsx3 speech engine
engine = pyttsx3.init()
engine.say(story)
engine.runAndWait()