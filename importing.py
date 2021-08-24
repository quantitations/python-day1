




################# IMPORTING OBJECTS FROM YOUR OTHER FILES #####################

# You can import variables, functions, or classes from other python files (called "modules" when being imported)

from workshop_misc import tao

tao[:100]

# Or you can import the whole module, then reference its objects with a dot

import workshop_misc
workshop_misc.tao[:100]

# If the module in question is in a subdirectory, indicate the relative path with dots.
# You can also give a nickname to any imported module or object.

import utility.more as m

m.previewParagraphs(tao)
m.previewParagraphs(tao, 100)



# Importing a class you've defined elsewhere then making use of it
## (more practice with classes)

from workshop_misc import Card


my_card = Card(rank=12, suit="hearts")
my_card

your_card = Card(rank=13, suit="clubs")
my_card.war(your_card)

another_card = Card(rank=12, suit="clubs")
my_card.war(another_card)






########################### PACKAGES/MODULES ##########################

# A module is a python file that defines objects
# that you might find helpful elsewhere.
# A package is a collection of modules.

# Many important packages come "built-in" to your python installation


import os
os.listdir()

import os, sys # import multiple modules in a single line
sys.version

from os import listdir, getcwd # import multiple objects in a single line
getcwd()

from os import listdir as ls, getcwd as wd # import multiple objects with nicknames in a single line
wd()




# Where is the python interpreter looking to find these modules?
sys.path

# I'm going to browse the directory C:\Users\12565\Anaconda3\Lib
# to see what files it contains...





# Let's define another class Deck that involves the class Card
# and makes use of the important built-in package "random"

import random

class Deck:
    
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in range(2, 15) for suit in ["spades", "hearts", "clubs", "diamonds"]]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def drawFromEnd(self, n):
        return [self.cards.pop() for i in range(n)]
    
    def addToEnd(self, cards):
        self.cards.extend(cards)


my_deck = Deck()
my_deck.cards

my_deck.shuffle()
my_deck.cards

n = 5

my_hand = my_deck.drawFromEnd(n)
my_hand

your_hand = my_deck.drawFromEnd(n)
your_hand

for i in range(n):
    my_hand[i].war(your_hand[i])










##################### PACKAGE MANAGEMENT ############################

# In addition to the packages we've seen, such as os, and sys, there are
# countless others that also extend the functionality of the Python language.
# If you installed Python via Anaconda Distribution, several thousand
# such packages are listed in Environments tab of Anaconda Navigator.
# With the click of a button, any chosen package will be downloaded
# and installed; then all of the functions and objects defined by that package
# become available to you with a single "import" command.
# In this same Environments tab, you can also update any package for which
# a newer version has been released.

# Alternatively, in a terminal, the command
# conda install package-name
# can also be used to update or install a package.

# In both cases above, the available packages are those listed in the "conda-forge" repository
# https://anaconda.org/conda-forge/repo

# Another program for package management is "pip" which works similarly to conda:
# pip install package-name
# looks for the package in the Python Package Index (PyPI) by default.
# https://pypi.org/
# pip can also install from other sources including github, e.g.
# https://adamj.eu/tech/2019/03/11/pip-install-from-a-git-repository/


# Realize that it's possible that code you've already
# written may actually stop working once you update a package.
# To prevent this issue, you can look into using "virtual environments"
# which we'll talk about later in this workshop.









