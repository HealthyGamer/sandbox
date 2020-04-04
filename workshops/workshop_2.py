# assigning values on initialization
pokemons = ['Pikachu', 'Mewtwo', 'Celebi']
print(pokemons)
 
# empty --> append values
pokemons = []
pokemons.append('Pikachu')
pokemons.append('Mewtwo')
pokemons.append('Celebi')
print(pokemons)
 
# EXERCISE #1
# Append your own pokemon to the list.
# and print iter
 
pokemons.append('Charizard')
print(pokemons)
 
print('First pokemon: ' + pokemons[0])
 
# EXERCISE #2
# print the last pokemon of your list.
print('Last pokemon: ' + pokemons[3])
print('Last pokemon: ' + pokemons[-1])
 
# Overwrite pokemon in first party position
pokemons[0] = 'Gyarados'
print(pokemons)
print('###############################')
 
# print(pokemons)
# temp = pokemons[0]
# print(pokemons)
# pokemons[0] = pokemons[1]
# print(pokemons)
# pokemons[1] = temp
# print(pokemons)
 
# EXERCISE #3
# swap first and last pokemon with temporary variable
# print the list after switch.
# use the -1 index notation if you want.
print(pokemons)
temp = pokemons[0]
print(pokemons)
pokemons[0] = pokemons[-1]
print(pokemons)
pokemons[-1] = temp
print(pokemons)
 
pokemon_in_party = len(pokemons) # integer
print('Party Size: ' + str(pokemon_in_party))
print(pokemons[pokemon_in_party - 1])
 
print('##########################')
 
# print('Before delete: ' + str(pokemons))
 
# del pokemons[1]
 
# print('After delete: ' + str(pokemons))
 
print('Before insert: ' + str(pokemons))
 
pokemons.insert(3, 'Slugma')
 
print('After insert: ' + str(pokemons))
 
# pokemons.clear()
# print(pokemons)
# EXERCISE #4
# use a while to print all pokemons in our party (one by one) (pokemons list)
# you need to increment your index, each time you go through the loop
index = 0 
# while condition|boolean:
#    do stuff here
# < > <= >= == !=
 
# while index < len(pokemons):
#   print(index)
#   print(index < len(pokemons))
#   print(pokemons[index])
#   index = index + 1
# print(index)
# print(index < len(pokemons))
 
pikachu_lvl = 1
 
# make a loop where pikachu gains 1 level per loop execution
# break when it reaches level 50
while pikachu_lvl < 50:
  pikachu_lvl = pikachu_lvl + 1
 
# print('Pikachu is now lvl: ' + str(pikachu_lvl))
# print('Pikachu is evolving !')
 
# use_thunderstone = True
# print('using thunderstone: ' + str(use_thunderstone))
 
# print('pikachu is lvl 50: ' + str(pikachu_lvl == 50))
 
# print('using thunderstone and pikachu is lvl 50: ' + str(use_thunderstone and pikachu_lvl == 50))
 
 
# if use_thunderstone and pikachu_lvl == 50:
#   print('Pikachu is now lvl: ' + str(pikachu_lvl))
#   print('We\'re using a thunderstone')
#   print('Pikachu is evolving !')
 
# age = 18
# has_beard = True
 
# if not age >= 21 and not has_beard:
#   print('You\'re out.')
# else:
#   print('You\'re in.')
 
# LAST EXERCISE
# 1st step declare variables for your pokemon's health and attack
# 2 pokemons --> 4 variables
pikachu_atk = 10
pikachu_hp = 50
 
pidgey_atk = 8
pidgey_hp = 55
 
from random import randint
 
a = randint(1, 10)
print(a)
 
while True:
  dmg = randint(0, pidgey_atk)
  pikachu_hp -= dmg
  print('Pidgey deals: ' + str(dmg) + ' dmg')
  print('Pikachu HP: ' + str(pikachu_hp))
  # condition and break here
  if pikachu_hp <= 0:
    print('Pikachu has fainted')
    break
 
  dmg = randint(0, pikachu_atk)
  pidgey_hp -= dmg
  print('Pikachu deals: ' + str(dmg) + ' dmg')
  print('Pidgey HP: ' + str(pidgey_hp))
  # condition and break here
  if pidgey_hp <= 0:
    print('Pidgey has fainted')
    break
 
print('Pidgey hp: ' + str(pidgey_hp))
print('Pikachu hp: ' + str(pikachu_hp))
print('We broke out of the loop.')
 
 
# Feel free to add misses and for an advanced addition, we can have critical strikes.
