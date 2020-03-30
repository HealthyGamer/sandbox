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
