import collections
from random import choice


Card = collections.namedtuple("Card", ["rank", "suit"])

"""
an iterable is any Python object with an __iter__() method or with a __getitem__() method that implements Sequence semantics
Iterable is an object, that one can iterate over. It generates an Iterator when passed to iter() method. 
An iterator is an object, which is used to iterate over an iterable object using the __next__() method. 
Iterators have the __next__() method, which returns the next item of the object.

Note: Every iterator is also an iterable, but not every iterable is an iterator in Python.

For example, a list is iterable but a list is not an iterator. 
An iterator can be created from an iterable by using the function iter(). 
To make this possible, the class of an object needs either a method __iter__, which returns an iterator,
or a __getitem__ method with sequential indexes starting with 0. 

We know that str is iterable but it is not an iterator. 
where if we run this in for loop to print string then 
it is possible because when for loop executes it converts into an iterator to execute the code

next("GFG")
Traceback (most recent call last) ...

s="GFG"
s=iter(s)
print(next(s))
"""


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()


print(len(deck))
# 52

print(deck[0])
# Card(rank='2', suit='spades')

print(choice(deck))
# Card(rank='K', suit='clubs')

for card in deck:
    print(card)
# Card(rank='2', suit='spades')
# Card(rank='3', suit='spades')
# ...

print(Card("Q", "hearts") in deck)
# True
print(Card("7", "beasts") in deck)
# False
