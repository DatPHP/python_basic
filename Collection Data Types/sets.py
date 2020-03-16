# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
thisset = {"banana", "strawberry", "berry"}
print(thisset)
print(type(thisset))
for x in thisset:
    print(x)

# Change Items
# Add items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Add multiple items to a set, using the update() method:
thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)
# Get the number of items in a set:
print(len(thisset))

# delete
thisset.remove("banana")
print(thisset)

# Note: If the item to remove does not exist, remove() will raise an error.


# Remove "banana" by using the discard() method:
#If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("mango")
thisset.discard("banana")

print(thisset)
""" 
You can also use the pop(), method to remove an item, but this method will remove the last item. 
Remember that sets are unordered, so you will not know what item that gets removed.

"""
x = thisset.pop()
print(x)
print(thisset)

# Sets are unordered, so when using the pop() method, you will not know which item that gets removed.

# clear() method empties the set:

# thisset.clear()

print(thisset)

# The del keyword will delete the set completely:

del thisset

# print(thisset) error because thisset is deteted.

# Join Two Sets

"""
use the union() method that returns a new set containing all items from both sets,
 or the update() method that inserts all the items from one set into another:
"""

# The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c", 3}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b", "c", 3}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
'''
There are other methods that joins two sets and keeps ONLY the duplicates, or NEVER the duplicates, check the full list of set methods in the bottom of this page.
'''
# set() Constructor

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)



