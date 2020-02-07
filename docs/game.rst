Game
====

Simple fighting game.

Players
-------

First we need player in order for our game to work. Each player is just a set
of stats, we group and represent them using
`dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
with the attribute names being
`strings <https://docs.python.org/3/library/stdtypes.html#str>`_ and their
values being their respective type (
`integers <https://docs.python.org/3/library/functions.html#int>`_ here).

.. code-block:: py

  {'health': 50, 'damage': 5}

We create **dicts** by wrapping :code:`key: value` pairs in :code:`{}`.

Variables
^^^^^^^^^

In order to store data somewhere so we can *reference* and use later we use
variables. In this case, we will name our two players in recognisable ways.

Usage
^^^^^

.. code-block:: py

  player1 = {'health': 50, 'damage': 5}
  player2 = {'health': 50, 'damage': 5}

Our players are identical to begin with.

Damage
------

Now we need to make the first operation of our game, dealing damage.

Modules
^^^^^^^

To introduce some level of "randomness", we use the built-in
`random <https://docs.python.org/3/library/random.html>`_ module.

Modules are chunks of code that other people have written for our use.

Importing modules can be done with
`import <https://docs.python.org/3/reference/simple_stmts.html#import>`_. In
this case, we need its
`randint <https://docs.python.org/3/library/random.html#random.randint>`_
function.

.. code-block:: py

  from random import randint

Python offers a variety of other built-in modules, we will take look at more of
them as we go.

Usage
^^^^^

But for now, let's deal some damage.

.. code-block:: py

  minimum = 1
  maximum = player1['damage']

  damage_dealt = randint(minimum, maximum)

We assign our **minimum** and **maximum** (from our player with
the item access :code:`[]` notation) damage to variables and then pass
those in the :code:`randint` function, creating a random integer and then
storing it in the :code:`incoming` variable.

To avoid redundancy and be a little bit quicker in our code:

.. code-block:: py

    damage_dealt = randint(1, player1['damage'])

Instead of storing our **min** and **max** in variables, we pass them directly
to the function.

Now, all we have to do is deduce this damage from the *other* player's health.

.. code-block:: py

  old_health = player2['health']
  new_health = old_health - damage_dealt
  player2['health'] = new_health

Or, we little bit faster:

.. code-block:: py

  player2['health'] = player2['health'] - damage_dealt

**EVEN FASTER**:

.. code-block:: py

  player2['health'] -= damage_dealt

All three ways are equivalent with the only significant difference being less
lines of code, making the whole thing more compact. Use whichever you are more
comfortable with.

Printing
^^^^^^^^

Now we need to show how much damage was dealt and how much health is left.

.. code-block:: py

  new_health = player2['health']
  message = f'Player 2 took {damage_dealt} damage: {new_health} health left'
  print(message)

Aside from normal strings starting and ending with the same type of quotes
(single or double), python offers
`f-string <https://docs.python.org/3/whatsnew/3.6.html#pep-498-formatted-string-literals>`_\s
for quickly formatting/injecting/interpolating data.

In this example, we simply pass our variables in an f-string, storing them in
the :code:`message` variable, which we then print to the console using the
built-in `print <https://docs.python.org/3/library/functions.html#print>`_
function.

Repeating
---------

All that's left now is to repeat the exact same process for :code:`player2`
attacking :code:`player1`.

.. code-block:: py

  damage_dealt = randint(1, player2['damage'])
  player1['health'] -= damage_dealt
  print(f'Player 1 took {damage_dealt} damage: {player1["health"]} health left')

We don't need to re-import the :code:`randint` function, this is done once at
the very beginning of our code.

The only notable difference between what we did before and now is printing. Not
only did we pass our string directly in :code:`print`, without using a
:code:`message` variable, we also messaged player1's health directly.

In order to differentiate between the start-end string quotes and the
:code:`health` string, different quotes had to be used.

Loops
^^^^^

So far, our code looks exactly like this:

.. code-block:: py

  from random import randint

  player1 = {'health': 50, 'damage': 5}
  player2 = {'health': 50, 'damage': 5}

  damage_dealt = randint(1, player1['damage'])
  player2['health'] -= damage_dealt
  print(f'Player 2 took {damage_dealt} damage: {player2["health"]} health left')

  damage_dealt = randint(1, player2['damage'])
  player1['health'] -= damage_dealt
  print(f'Player 1 took {damage_dealt} damage: {player1["health"]} health left')

player1 attacks player2, and vice versa and our program exits. Obviously, we
need this to happen multiple times until either of the players falls
to-or-bellow :code:`0` health. Or, in other words, we need our program to *loop*
back to the beginning *while* both players are above :code:`0` health.

Conveniently, this can be done with a
`while loop <https://docs.python.org/3/reference/compound_stmts.html#while>`_.

.. code-block:: py

  while player1['health'] > 0 and player2['health'] > 0:
    damage_dealt = ...

Comparisons
^^^^^^^^^^^

Let's take a look at what's going on.

.. code-block:: py

    player1['health'] > 0

This statement will, unsurprisingly, return
`True <https://docs.python.org/3/library/constants.html#True>`_ if player1's
health is above :code:`0` health, and
`False <https://docs.python.org/3/library/constants.html#False>`_ otherwise.

 .. code-block:: py

  player1['health'] > 0 and player2['health'] > 0

Here we get :code:`True` if both players' health is above :code:`0`, and
:code:`False` otherwise.

While
^^^^^

Our while loop needs a statement that returns :code:`True` or :code:`False`
next to it. That statement is executed on every iteration, stopping the loop
the moment it evaluates to :code:`False`.

.. code-block:: py

  while player1['health'] > 0 and player2['health'] > 0:
    damage_dealt = randint(1, player1['damage'])
    player2['health'] -= damage_dealt
    print(f'Player 2 took {damage_dealt} damage: {player2["health"]} health left')

    damage_dealt = randint(1, player2['damage'])
    player1['health'] -= damage_dealt
    print(f'Player 1 took {damage_dealt} damage: {player1["health"]} health left')

Anything that is part of the loop's execution should be indented inward.

Each player's health will get decreased on each iteration, until at least one is
not above ``0``. The main caveat of this approach the possibility that both
players' health gets reduced bellow ``0``, resulting in a **trade-kill**.

Break
^^^^^

To prevent this from happening, we take a slightly different approach.

.. code-block:: py

  while True:

    damage_dealt = randint(1, player1['damage'])
    player2['health'] -= damage_dealt
    print(f'Player 2 took {damage_dealt} damage: {player2["health"]} health left')

    if player2['health'] <= 0:
        print('Player 1 wins')
        break

    damage_dealt = randint(1, player2['damage'])
    player1['health'] -= damage_dealt
    print(f'Player 1 took {damage_dealt} damage: {player1["health"]} health left')

    if player1['health'] <= 0:
      print('Player 2 wins')
      break

We create an **infinite loop** by giving :code:`while` something that always
evaluates to :code:`True`. That could be :code:`1 > 0`, :code:`'hg' == 'hg'`, or
simply :code:`True` itself.

This allows us sequentially check whether each player's health is at-or-bellow
:code:`0`:

.. code-block:: py

  if player2['health'] <= 0:
    print('Player 1 wins')
    break

If :code:`player2['health'] <= 0` returns :code:`True`, everything in our
:code:`if` clause (indented code) gets executed; printing who won and then
`break <https://docs.python.org/3/reference/simple_stmts.html#break>`_\ing
out of the loop.

Recap
-----

And behold our final result.

.. code-block:: py

  from random import randint

  player1 = {'health': 50, 'damage': 5}
  player2 = {'health': 50, 'damage': 5}

  while True:

    damage_dealt = randint(1, player1['damage'])
    player2['health'] -= damage_dealt
    print(f'Player 2 took {damage_dealt} damage: {player2["health"]} health left')

    if player2['health'] <= 0:
        print('Player 1 wins')
        break

    damage_dealt = randint(1, player2['damage'])
    player1['health'] -= damage_dealt
    print(f'Player 1 took {damage_dealt} damage: {player1["health"]} health left')

    if player1['health'] <= 0:
      print('Player 2 wins')
      break

Something to consider is that this game is skewed toward player1 since they
always strike first ;)
