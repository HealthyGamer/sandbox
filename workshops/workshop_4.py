# Syntax

def calc(a, b):
  result = a + b
  return result

result = calc(3, 4) # 7
print(result)

# Exercise
# Make a function that divides two numbers

# Answer
def div(a, b):
  return a / b

# Argument names and default arguments (keyword parameters)

def calc(a, b, m = 1, e = 5):
  return (a + b) * m + e

result = calc(2, 8) # 15
print(result)
result = calc(2, 8, 2, 0) # 20
print(result)
result = calc(2, 8, e = 0) # 10
print(result)
result = calc(2, 8, e = 2, m = 0.6) # 8
print(result)

# Exercise
# Find a combination of arguments that results in 6.5 without using "e"

# Answer
# calc(1, 2, m = 0.5)

# Using multiple

def add(a, b):
  return a + b

def mul(a, b):
  return a * b

result = add(3, 2) + mul(5, 2) # 15
print(result)

# Using function results in other functions

added = add(3, 2) # 5
multd = mul(added, 2) # 10

# Or directly

result = mul(add(3, 2), 2) # 10

# Using funtions in other functions

# We had this
# def calc(a, b, m = 1, e = 5):
#   return (a + b) * m + e

# Now we redefine it
def calc(a, b, m = 1, e = 5):
  added = add(a, b)
  multd = mul(added, m)
  final = add(multd, e)
  return final

# Or directly

def calc(a, b, m = 1, e = 5):
  return add(mul(add(a, b), m), e)

result = calc(2, 8, e = 2, m = 0.6) # 8
print(result)

# Exercise
# Incorporate your division function so "calc" returns "((a + b) * m + e) / d" where d is the overall denominator with a default value of 1
# Change calc so that the result is divided by a new variable 'd' before being returned (use the "div" function) with a default value of 1

# Answer
def calc(a, b, m = 1, e = 5, d = 1):
  return div(add(mul(add(a, b), m), e), d)

def make_description(pokemon):
  name = pokemon['name']
  level = pokemon['level']
  message = 'Pokemon ' + name + ' is level ' + str(level)
  return message

def show_description(pokemon):
  message = make_description(pokemon)
  print(message)

pokemon = {
  'name': 'Magikarp',
  'level': 94,
  'health': 348
}

show_description(pokemon)

# ################
# PART 2
# ################

# Changing objecs that contain other objects in functions changes them outside as well

def level_up(pokemon):
  pokemon['level'] += 1
  # no need to return

print(pokemon)
level_up(pokemon)
print(pokemon)

# Functions also have access to variables in their outer scope

m = 1
def add(a, b):
  return (a + b) * m

result = add(3, 2) # 5
print(result)

m = 2

result = add(3, 2) # 10
print(result)

# This is what allows functions to use other functions, because functions are actually just variables

# Exercise
# make a function that takes user input and adds it to a list outside of the function's scope
# do it with pokemon names!

# Answer

pokes = []

def new_poke(shiny = False):
  poke = input()
  if shiny:
    poke = 'Shiny ' + poke
  pokes.append(poke)

new_poke()
new_poke()
new_poke(shiny = True)

# Variable amount of arguments
# Sometimes, functions are defined to handle any amount of arguments

def add(*nums):
  result = 0
  for num in nums:
    result += num
  return result

result = add(2, 3, 8, -4, 9) # 18
print(result)

# Same goes for keyword arguments

def backpack(**stuff):
  keys = stuff.keys()
  for key in keys:
    amount = stuff[key]
    print('You have ' + str(amount) ' of ' + key)

# Quicker version

def backpack(**stuff):
  for (thing, amount) in stuff.items():
    print('You have ' + str(amount) ' of ' + thing)

# And a combination of both

def somefunc(*args, **kwargs):
  print(args)
  print(kawrgs)

# Mention how print also takes multiple arguments!

somefunc(3, True, 'hi', abc = 123, happy = 'sad')

# Creative

poke1 = {
  'name': 'Victini',
  'attack': 1.2,
  'defense': 0.91,
  'health': 118,
  'moves': [
    {
      'name': 'Quick Attack',
      'power': 23
    },
    {
      'name': 'Inferno',
      'power': 41
    }
  ]
}

poke2 = {
  'name': 'Milotic',
  'attack': 1.03,
  'defense': 0.86,
  'health': 130,
  'moves': [
    {
      'name': 'Tackle',
      'power': 26
    },
    {
      'name': 'Wrap',
      'power': 38
    }
  ]
}

# choice picks a random element from a list
# sample gives a shuffled sublist from a list
from random import choice, sample

def calc_dmg(poke1, poke2, move):
  return round(move['power'] * poke1['attack'] * poke2['defense'])

def attack(poke1, poke2):
  move = choice(poke1['moves'])
  damage = calc_dmg(poke1, poke2, move)
  print(poke1['name'] + ' used ' + move['name'] + ' for ' + str(damage) + ' damage!')
  health = poke2['health']
  health = max(0, health - damage)
  poke2['health'] = health
  print(poke2['name'] + ' dropped to ' + str(health) + ' health.')

def fight(*pokes):
  pokes = sample(pokes, 2)
  poke1 = pokes[0]
  poke2 = pokes[1]
  while True:
    print('-' * 30)
    attack(poke1, poke2)
    if poke2['health'] <= 0:
      print(poke2['name'] + ' fainted, ' + poke1['name'] + ' wins!')
      break
    print('-' * 10)
    attack(poke2, poke1)
    if poke1['health'] <= 0:
      print(poke1['name'] + ' fainted, ' + poke2['name'] + ' wins!')
      break

fight(poke1, poke2)
