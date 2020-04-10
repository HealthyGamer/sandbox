pokemon = {'name': 'Pikachu', 'level': 7, 'male': True}

def levelup(pokemon):
  pokemon['level'] += 1
  print('Pokemon', pokemon['name'], 'leveled up to', pokemon['level'])

levelup(pokemon)

# curveball

floor = {
  'name': 'Office',
  'level': 2,
  'clean': True
}

levelup(floor)

# class syntax

print('Using classes...')

class Pokemon:
  def __init__(self, name, level = 1, male = None):
    self.name = name
    self.level = level
    self.male = male
  def levelup(self):
    self.level += 1
    print('Pokemon', self.name, 'leveled up to', self.level)

pokemon = Pokemon('Pikachu', 7, True)

pokemon.levelup()

other_pokemon = Pokemon('Squirtle', 97, False)

other_pokemon.levelup()

# instances...

print(pokemon.name, pokemon.level, pokemon.male)

pokemon.level += 1

print(pokemon.level)

pokemon.__dict__['level'] -= 1

print(pokemon.level)

# Exercise - Make a "Trainer" class with "name", "gender" and "age" attributes
# Continue - Add an "introduce" method, printing all attributes of the class in a nice manner

class Trainer:
  def __init__(self, name, gender, age = 10):
    self.name = name
    self.gender = gender
    self.age = age
  def introduce(self):
    print('Hello, my name is', self.name, ', Im a', self.gender, 'and', self.age, 'years old!')

trainer = Trainer('Holly', 'female', age = 23)

trainer.introduce()

class Named:
  def __init__(self, name):
    print("Hey we are in the Named class")
    self.name = name
  
  def describe(self):
    print('This is a', self.__class__.__name__, 'called', self.name)

class Item(Named):
  def __init__(self, price, name):
    super().__init__(name)
    self.price = price
  
  def describe(self):
    super().describe()
    print('Sells for', self.price)

class Pokemon(Named):
  def __init__(self, moves, name, attack, defense, health, level = 1, male = None):
    super().__init__(name)
    self.moves = moves
    self.level = level
    self.male = male
    self.health = health
    self.defense = defense
    self.attack = attack

  def inflict_damage(self, pokemon, move_name):
    selected_move = None
    for move in self.moves:
      if move.name == move_name:
        selected_move = move
        break
    inflicted_damage = (self.attack * 0.1 * selected_move.power) - pokemon.defense
    pokemon.health -= inflicted_damage
    print(self.name, 'inflicts', inflicted_damage, 'damage to', pokemon.name)


geodude_moves = [
  Move('tackle', 15),
  Move('earthquake', 25)
]

geodude = Pokemon(geodude_moves, 'Geodude', 20, 30, 200, level = 15, male = True)

geodude.describe()

pikachu_moves = [
  Move('tackle', 15),
  Move('thunder', 25)
]

pikachu = Pokemon(pikachu_moves, 'Pikachu', 45, 15, 150, level = 14, male = False)

print('Geodude\'s health', geodude.health)
pikachu.inflict_damage(geodude, 'thunder')
print('Geodude\'s health', geodude.health)
