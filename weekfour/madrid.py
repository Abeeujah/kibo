# See the Instructions tab.
# Scroll down to see where you should write your solution
roster = [
    "Thibaut Courtois",
    "Dani Carvajal",
    "Brahim Díaz",
    "Éder Militão",
    "Jesús Vallejo",
    "Nacho",
    "Eden Hazard",
    "Toni Kroos",
    "Karim Benzema",
    "Takefusa Kubo",
    "Álvaro Odriozola",
    "Luka Modrić",
    "Marco Asensio",
    "Marcelo",
    "Andriy Lunin",
    "Martin Ødegaard",
    "Casemiro",
    "Federico Valverde",
    "Luka Jović",
    "Sergio Ramos",
    "Lucas Vázquez",
    "Gareth Bale",
    "Dani Ceballos",
    "Vinícius Júnior",
    "Raphaël Varane",
    "Rodrygo",
    "Isco",
    "Ferland Mendy",
    "Mariano"
]

# Write your solution below

print("\nThe current Real Madrid roster:\n")
# Print the current roster using a for loop
for player in roster:
    print(player)

print("\n------")
# Remove players using pop()
pop_list = [2, 9, 10, 15, 19, 24]
track = 0
for i in pop_list:
    roster.pop(i - track)
    track += 1


# Add players using append()
app_list = ['Eduardo Camavinga', 'David Alaba']
for player in app_list:
    roster.append(player)

print("\n------")
print("\nThe new Real Madrid roster:\n")
# Print the new roster using a for loop
for player in roster:
    print(player)

# Function to print players
# def printPlayer(roster):
#     for player in roster:
#         print(player)
