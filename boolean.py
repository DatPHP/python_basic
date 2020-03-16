print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

a = bool("Nguyen Van DAt")
print(a)
print(type(a))

# Some Values are False
print(
    bool(False),
    bool(None),
    bool(0),
    bool(""),
    bool(()),
    bool([]),
    bool({}),
)


class myClass():
    def __len__(self):
        return 0


"""
One more value, or object in this case, evaluates to False, 
and that is if you have an object that is made from a class
 with a __len__ function that returns 0 or False:
"""
myobj = myClass()
print(bool(myobj))


# Functions can Return a Boolean

def myFunction():
    return True


print(myFunction())


def myFunction():
    return True


if myFunction():
    print("YES!")
else:
    print("NO!")

#isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))

