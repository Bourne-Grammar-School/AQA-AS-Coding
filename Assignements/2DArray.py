import random

# Task 1: print a 2D array of 8x8 zeros using for loops
# Your print out 2D array should look like :

'''
00000000
00000000
00000000
00000000
00000000
00000000
00000000
00000000
'''


# Task 2: define a function that generates a 2D array of 8x8 hyphens and print it out.
# Your print out 2D array should look like this:
'''
--------
--------
--------
--------
--------
--------
--------
--------
'''

# Task 3: use the 2D array you have generated above,
# define a function that adds a | between the hyphens when print it out.
# Your print out 2D array should look like :
'''
|-|-|-|-|-|-|-|-|
|-|-|-|-|-|-|-|-|
|-|-|-|-|-|-|-|-|
|-|-|-|-|-|-|-|-|
|-|-|-|-|-|-|-|-|
|-|-|-|-|-|-|-|-|
|-|-|-|-|-|-|-|-|
|-|-|-|-|-|-|-|-|
'''


# Task 4: use the 2D array you have generated on task3,
# Place the letter Z (zombie) randomly in the grid.

# Task 5: after Task 4,
# define a function that will locate the Z inside the grid

def getZPosition():
    # your code here

# Task 6: after Task 5,
# define a function that will move the Z by one step inside the grid by
# using WASD keys.


def moveZ(direction):
    # your code here

# Task 7: continue from the previous tasks,
# define a function that will randomly place the elements in the list, people
# in the 2D array.

people =['A','B','C','D','E']


# Task 8: continue from the previous tasks,
# define a function that will detecting
# when Z moves into one of the people in the grid.
# If so, change the person into Z.



# Task 9: extend from the previous tasks,
# add a game play loop, so that:
# 1) the program continues until all people turn into Z;
# 2) the people will move in a random direction each loop.
