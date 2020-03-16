thisList = ["apple", "orange", "bannaner"]
print(thisList)
print(thisList[1])
# Negative Indexing
print(thisList[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1:5])
"""
note: 
The search will start at index 2 (included) and end at index 5 (not included).
Remember that the first item has index 0.
"""
# returns the items from the beginning to "orange":
print(thislist[:4])
# This will return the items from index 0 to index 4.

# Remember that index 0 is the first item, and index 4 is the fifth item
# Remember that the item in index 4 is NOT included

# returns the items from "cherry" and to the end:
print(thislist[2:])

# This will return the items from index 2 to the end.

# Remember that index 0 is the first item, and index 2 is the third

# Specify negative indexes if you want to start the search from the end of the list:
# This example returns the items from index -4 (included) to index -1 (excluded)
print(thislist[-4:-1])
thislist[1] = "blackcurrant"
print(thislist)

# Loop Through a List

for x in thislist:
    print(x)
# Check if Item Exists
if "cherry" in thislist:
    print("yes")
# List Length
print("Do dai cua  list la: " + str(len(thislist)))

# Add Items
# To add an item to the end of the list, use the append() method:
thislist.append("strawberry")
print(thislist)

# To add an item at the specified index, use the insert() method:
thislist.insert(1, "aloooo ")
print(thislist)

# Remove Item

thislist.remove("mango")
print(thislist)

# pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop(1)
print(thislist)

# del keyword removes the specified index:
del thislist[1]
print(thislist)

# clear() method empties the list:
"""
thislist.clear()
print(thislist)
"""

# Copy a List
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().
mylist = list(mylist)
print(mylist)

# Join Two Lists
list1 = ["a", "b", "c", 1, 2]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# use the extend() method, which purpose is to add elements from one list to another list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

thislist = list(("apple", "banana", "cherry"))
print(thislist)

newlist = list(("k", "a", "l", "b"))
newlist1 = newlist.reverse()
print(newlist1)