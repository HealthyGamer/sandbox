# Understanding Types

# Syntax Reminder
class Calc:
  def __init__(self, a, b = 3):
    self.a = a
    self.b = b
  def do(self):
    return self.a + self.b

# Instance Creation
calc = Calc(5)
result = calc.do()
print(result)

# Python comes with a few built-in classes (or "types") that we've been using a lot so far
print(str, int, float, bool, list, dict)
# And some more less used ones
print(tuple, set, frozenset, bytes, bytearray)

# Python offers ways to create instances of these classes without calling them
'Hello World!', 6, 9.4, True, [], {}

# But that doesn't mean that we can't call their classes for additional functionality
print(str(True)) # 'True'
print(int('4')) # 4
print(float('.2')) # 0.2
print(bool(0)) # False
print(list('abcde')) # ['a', 'b', 'c', 'd', 'e']
print(dict()) # {}

# And just like custom class instances, they have methods built-into them.

x = ' Hello World!'
print(x)
x = x.lower()
print(x)
x = x.title()
print(x)
weird_x = x.replace('o', 'u')
print(weird_x)
l_count = x.count('l')
print(l_count)
words = x.split(' ')
print(words) # one empty string
x = x.strip()
print(x)
# And many more...

# A list of every attribute and function of each instance (or class) can be obtained with "dir".
print(dir(x))

# You can see information about what each method does by calling "help" on it
help(float.as_integer_ratio) # the interpreter will block until you press "q"

# Exercise - Given a string (ex: 'aesthetic') create an aesthetic string ('A E S T H E T I C').

# Answer - Long
x = 'aesthetic'
x = x.upper().split()
x = ' '.join(x)

# Answer - Short
x = 'aesthetic'
x = ' '.join(x).upper()

# Exercise - Merge two dictionaries into a new dictionary.
# Hint: Copy one of them, creating a completely new dictionary and then merge the other with it.

# Answer
a = {'one': 'thing'}
b = {'two': 2}

c = a.copy()
c.update(b)

# Just like custom classes, built-in ones are subject to inheritance and can be subclassed

class MyStr(str):
  def five_of(self, value):
    return self.count(value) == 5

# This is a "str" instance but not a "MyStr" instance so it doesn't have "five_of".
x = 'whoooooa'

x = MyStr('whoooooa')
print(x)
print(x.five_of('u'))
print(x.five_of('o'))

# Next Half

dir(int) # ['__add__', '__class__', '__contains__', '__delattr__', ...

# There are called "dunder", "special" or "magic" variables.
# They are always set (and usually managed by) python itself and dictate functionalities.

# For example, int.__gt__ is a method that tells us if a number is greater than another number
x = 5
print(x.__gt__(7))
print(x > 7)
# These are the same thing!

# We can overwrite these methods with inheritance to change their behaviour
# int.__add__ dictates what the + operator does
class MyInt(int):
  def __add__(self, other):
    return self - other

a = MyInt(9)
print(a)
b = a + 6
print(b) # normally 15 but it's 3

a = MyInt(4)
print(a)
b = 4 + a # 8, not 0! Because int's __add__ is used here.
print(b)

# There are a lot of dunder methods and attributes like these, not all are meant to be overwritten.
# The most common one to overwrite is the __init__ method! (You already know that).

# Truth is, every normal class is actually an implicit subclass of "object".
# When we create a class, we overwrite the object's __init__ method which normally does nothing.

class MyX(object):
  def __init__(self):
    self.x = 4

class MyX:
  def __init__(self):
    self.x = 4

# These are the same thing! In fact, older versions of pyhon always used the first notation.

# Exercise - Make a pokemon class that, when instances are added together, combine their stats.
# Stats should be "name"(str), "health"(int)
# "name" should be combined with a space using "str.join"
# "health" should be added normally
# Finally, return a new Pokemon class using self.__class__

# Answer

class Pokemon:
  def __init__(self, name, health):
    self.name = name
    self.health = health
  def __add__(self, other):
    # name
    name = ' '.join([self.name, other.name])
    # health
    health = self.health + other.health
    # why use self.__class__ instead of Pokemon directly?
    return self.__class__(name, health)
  def __repr__(self):
    # Do this after the exercise
    return f'Pokemon({self.name},{self.health})'

poke1 = Pokemon('Pikachu', 53)
print(poke1)
poke2 = Pokemon('Spinda', 12)
print(poke2)
poke3 = poke1 + poke2
print(poke3)

# We can add a lot together
poke4 = Pokemon('Bastiodon', 94) + Pokemon('Hattrem', 76) + Pokemon('Chansey', 41)
print(poke4)

# Exercise - Make a list with a ".add" method that creates, appends and returns a pokemon
# Hint: Use *args to supply the class with the method's arguments
# Extra - Make it so that the len() of the list only returns the amount of alive pokemon (health > 0)

class Party(list):
  def add(self, *args):
    poke = Pokemon(*args)
    self.append(poke)
    return poke
  def __len__(self):
    alive = []
    for poke in self:
      if poke.health > 0:
        alive.append(poke)
    return len(alive)

party = Party()
party.add('Venipede', 12)
party.add('Seedot', 30)
party.add('Kricketot', 0)
party.add('Drilbur', 32)
print(party)
print(len(party))

# Good practice? No! This is all for learning purposes.

# type(x) gives the class of an instance "x" (same as doing x.__class__)

type(party) # class 'Party'
type([]) # class 'list'
type(party.add) # class 'method'
type(Party.add) # class 'function'

# methods are bound to instances
# funcions are not, in fact, class-level functions are not bound to anything and can be used as-is

# So, as long as we pass the appropriate arguments, they should still work
x = []
Party.add(x, 'Sobble', 65)
print(x)

# Although x is not an instance of Party, it was a valid argument for add
# To understand this a bit better, go ahead and replace "self" with "x" in Party.add
# class functions are just wannabe methods, but are not methods yet!
# We could not have done this with an instance's .add method, because "self" is passed automatically
# So we would end up passing "self" AND "x", where "x" would take the spot of "name" (not cool)

# Exercise - Using your actual party instance, get the total amount of pokemon (not just alive)
# Careful: Do not use loops!

# Answer
total = list.__len__(party)
