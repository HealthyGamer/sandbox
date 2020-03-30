#List of strings: pokemon names
pokemons = ['Mienfoo', 'Snover', 'Medicham', 'Vulpix', 'Skarmory', 'Snorunt'];

#while loop
i = 0
while i < len(pokemons):
  pokemon = pokemons[i]
  print('index: ' + str(i)) 
  print('pokemon: ' + pokemon) 
  i += 1

#for in loop: only the values are accesible
#['Mienfoo'], ['Snover]
for pokemon in pokemons:
  print('pokemon: ' + pokemon) 

#for in loop + enumerate: index and value are accessible 
#[0, 'Mienfoo'], [1, 'Snover]
#[i, pokemon]
for i, pokemon in enumerate(pokemons):
  print('index: ' + str(i)) 
  print('pokemon: ' + pokemon) 

#Closer to a C-style for loop: for(i = 0; i < len(pokemon); i ++)
for i in range(0, len(pokemons)):
  print('index: ' + str(i)) 
  print('pokemon: ' + pokemons[i]) 


#Excercise 1

#Loop and take input from user to create pokemon names
#add pokemon names to pokemons list
#STOP the loop, when the user inputs 'DONE'

#print out all pokemon in the list

#some component pieces.
# pokemons = []
# print('Enter a pokemon')
# value = input()
# if value == 'DONE':

pokemons = []
while True:
    print("Type a name to add to the list, or type DONE to exit")
    value = input();
    if value == 'DONE':
        break;
    pokemons.append(value);

for pokemon in pokemons:
    print(pokemon)

    
# EXERCISE #2 - Empty the list without .clear

# ANSWER (EXPECTED)
for pokemon in pokemons:
  pokemons.remove(pokemon) # doesn't work!
  
# ANSWER
while len(pokemons) > 0:
  del pokemons[0]

# Introduce dictionary
# We will create a dictionary for a single discord user
user = {
  'name': 'Exa', 
  'tag': 7448,
  'avatar': 'htps://linktoimage.jpg'
}

# Change value of specific key in a dictionary
user['tag'] = 7445

# Delete item (key/value pair) in dictoinary
del user['avatar']

# Set a new item (key/value pair) in dictionary
user['avatar'] = 'https://linktocoolerimage.png'

# Get the keys
keys = user.keys()
print('Showing keys...')
for key in keys:
  print(key)

# Get the values
values = user.values()
print('Showing values...')
for value in values:
  print(value)

# Get key-value pairs
items = user.items()
print('Showing items...')
for item in items:
  print(item)
  
# Ask them to add to the keys/values/items like a list
# NOT a list! It's a dynamically updated, read-only "list".

user['status'] = 'All these squares make a circle'

print('Updated dictionary:')
print(items)

# EXERCISE #3 - Get the key of a value

# ANSWER
print('Getting key...')
for (key, value) in user.items():
  if value == 7445:
    break
print(key)

# Clear the dictionary
print('Empty user:')
user.clear()
print(user)

# SECOND HALF

pokemon = {
  'name': 'Bulbasaur',
  'types': ['Grass', 'Poison'],
  'health': 200,
  'level': 1,
  'moves': []
}

print('Your pokemon:')
print(pokemon)

# Print specific values
print(pokemon['name'])

# Show multiple values
print(pokemon['name'] + ' has ' + pokemon['health'] + 'hp') # Doesn't work!

# Use str() to convert integer to string
print(pokemon['name'] + ' has ' + str(pokemon['health']) + 'hp')

# Lets add a move
move = {
  'name': 'Tackle',
  'type': 'Normal',
  'power': 80,
  'accuracy': 75
}

# Print the move
print ('Your move:')
print(move)

# Two ways to add to our list of moves

# Long way
moves = pokemon['moves']
moves.append(move)

print('Your pokemon:')
print(pokemon)

# Short way
pokemon['moves'].append(move)

print('Your pokemon:')
print(pokemon)

# Make a party (list of pokemons)
pokemons = [pokemon]

# EXERCISE #4: Make your own and add them to the party

# SOLUTION
while True:
  print('Enter the name of a Pokemon:')
  name = input()
  print('Enter health of Pokemon:')
  health = input()
  print('Enter level of Pokemon:')
  level = input()
  
  newpokemon = {
    'name': name,
    'health': health,
    'level': level
  }

  pokemons.append(newpokemon)

  print('Would you like to add another? (Y/n)')
  another = input()
  if another.lower() == 'n':
    break;

print('Your party:')
print(pokemons)

# Data structures in the real world

import requests
response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
print(response.json())

# More complex example

import requests

print('Enter pokemon name to look up:')
name = input()

response = requests.get('https://pokeapi.co/api/v2/pokemon/' + name.lower())

data = response.json()

abilities = data['abilities']

for ability in abilities:
  print(ability['ability']['name'])

# BONUS EXERCISE
# Level up Pokemon
# - Make the level go up by 1
# - Increase its health by 10%
# - If it only has one move, learn a new move
