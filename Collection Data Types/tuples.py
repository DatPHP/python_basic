# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])
# Negative Indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
print(thistuple[-1])
# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
# Note: The search will start at index 2 (included) and end at index 5 (not included).
# Remember that the first item has index 0.
# Range of Negative Indexes
print(thistuple[-4:-1])

# Change Tuple Values
x = ("banana", "cherry", "long")
# x[1] = "hello" ====== > error because tuple' object does not support item assignment
print(x)
y = list(x)
y[1] = "NGuyen Van Dat"
x = tuple(y)
print(x)

# Loop Through a Tuple
for x in thistuple:
    print(x)
# Check if Item Exists
if "dat" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
else:
    print("no")
    # Tuple Length
    # To determine how many items a tuple has, use the len() method:
    print(len(thistuple))

    # Create Tuple With One Item
    """
    To create a tuple with only one item,
     you have add a comma after the item,
      unless Python will not recognize the variable as a tuple.
    """
    thistuple = ("apple",)
    print(type(thistuple))
    # NOT a tuple
    thistuple = ("apple")
    print(type(thistuple))
    # Remove Items
    del thistuple
# print(thistuple) ===== > error because the tuple no longer exists
# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)



