'''
Write a function called `geq` which accepts two arguments `a` and `b`, in that order.
If `a` is greater than or equal to `b` it returns true otherwise it returns false.
'''

def geq(a, b):
    if a >=b:
        return "True"
    else:
        return "False"

'''
Write a function called `logical_mess` that accepts 3 arguments in the order `a`, `b`, `c`.

Whichever of the following conditions is encountered first should determine the return value of the function.

i.   If any one or more of the arguments are `None` the function should return -1. (None is NULL in Python)
ii.  If any two or more of the arguments are equal it should return 1.
iii. If all three arguments are equal it should return 2.
iv. If `c` is equal to 10 and `a` is not equal to 5 it should return 3.
v. If `c` is equal to 10 and `a` is equal to 5 it should return 4. 
vi. If `c` is greater than `10` and `a` is greater than `b` it should return 4. 
vii. Otherwise return 6
'''

def logical_mess(a, b, c):
    if a is None:
        return -1
    elif a == b:
        return 1
    elif a == b == c:
        return 2
    elif c == 10 and a != 5:
        return 3
    elif c ==10 and a == 5:
        return 4
    elif c > 10 and a > b:
        return 4
    else:
        return 6


'''
Create an Adventurer class. The class name should be Adventurer.
It should have the following properties:

gold - an integer that describes how much gold the adventurer has, it should never go below zero.
inventory - a list of items represented as strings in the adventurers inventory
name - a string representing the adventurer's name.

It should have the following methods:

Constructor ( str, int) - this will set the adventurers name and starting gold respectively.
  If starting gold is negative it should be set to 0.
lose_gold( int ) - this will cause the adventurer to lose gold the amount of gold specified but never
  go below zero. If it tries to go below zero it should set the adventurer's gold to zero and return
  False, otherwise it should return True.
win_gold( int ) - this will cause the adventurer to gain the amount of gold specified.
add_inventory( str ) - this will add the string to the adventurers inventory
remove_inventory( str ) - this will remove at most one copy of an item from the adventurer's
  inventory. It should return True if it removed an item or False if the item was not found
'''

class Adventurer:
    # constructor
    def __init__(self, name, gold):

        self.name = name

        self.gold = randint(0,100)

    #method 1
   def lose_gold(self, lose_gold):

       self.default_integer = 0

       if lose_gold < = 0:
           return 0
       else:
       return self.default_integer

    #method 2
    def win_gold(self, win_gold):

    #method 3
   def add_inventory(self, add_inventory):

    #method 4
    def remove_inventory(self, '')
        if item removed:
        return True
    else:
    return False