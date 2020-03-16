a = "Nguyen Van Dat"
print(a[1])
 
"""
slicing 
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
"""
print(a[3:6])
'''
Use negative indexes to start the slice from the end of the string:
'''
b = "Hello, World!"
print(b[-5:-2])
'''
String Length
To get the length of a string, use the len() function.
'''
print(len(a))
c = "   Hello, World!   "
print(c[-5:-2])
#len() function returns the length of a string:
print(len(c))
#strip() method removes any whitespace from the beginning or the end:
print(c)
print(c.strip())
#lower() method returns the string in lower case:
print(c.lower())
#upper() method returns the string in upper case:
print(c.upper())
#replace() method replaces a string with another string:
print(c.replace("l", "Day"))

d = "Nguyen, Van , dAT, LAP, tRINH pYTHON"
arr = d.split(",")
print(arr)

#Check String
#Check if the phrase "ain" is present in the following text:
x = "AT" in d
print(x)
# Check if the phrase "ain" is NOT present in the following text:
y = "d" not in d
print(y)



#String Concatenation
#To concatenate, or combine, two strings you can use the + operator.
a = "hello"
b = "word"
c = a +" "+ b
print(c)

# String Format
""" 
age = 36
txt = "My name is John, I am " + age
print(txt)

====> errror because As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
"""

""""
But we can combine strings and numbers by using the format() method!
"""
age = 24
name = "Nguyen Van Dat is {} year old "
tranName = name.format(age)
print(tranName)

# infor1 = name + " " + age
character = format(age)
print(type(character))
infor = name + " " + format(age)

print(infor)
#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

firstName = "Dat"
lastName = "Nguyen Van "
age = 24
fullInfor = "My name is {} {} . I am {}"
stringINfor = fullInfor.format(firstName, lastName, age)
print(stringINfor)

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

age = 24
fullInfor = "My name is {2} {0} . I am {1}"
stringINfor = fullInfor.format(firstName, lastName, age)
print(stringINfor)

# use the escape character \"
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\ xhh	Hex value
"""
