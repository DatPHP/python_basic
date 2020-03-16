"""
A dictionary is a collection which is unordered, changeable and indexed.
In Python dictionaries are written with curly brackets,
and they have keys and values.
"""
student = {
    "Mssv": 15139,
    "Name": "NGuyen Van DAT",
    "age": 23
}
print(student)

x = student["Name"]
print(x)
y = student.get("Name")
print(y)

# Change values
thisdict = {"brand": "Ford", "model": "Mustang", "year": 2018}

thisdict["year"] = 2019
print(thisdict)
# Loop Through a Dictionary
for x in thisdict:
    print(x)
# Print all values in the dictionary, one by one:
for x in thisdict:
    print(x + " :  " + str(thisdict[x]))

# use the values() function to return values of a dictionary:

for x in thisdict.values():
    print(x)
    print(type(x))

# Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
    print(x, y)

# Check if Key Exists
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
    # Dictionary Length
    # To determine how many items (key-value pairs) a dictionary has, use the len() method.
    print(len(thisdict))
    # Adding Items
    # Adding an item to the dictionary is done by using a new index key and assigning a value to it:
    thisdict["color"] = "red"
    print(thisdict)
    # Removing Items
    # The pop() method removes the item with the specified key name:
    thisdict.pop("model")
    print(thisdict)


