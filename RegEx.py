# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
import re

txt = "NGuyen Van Dat. I am styding Science of university"
# Check if the string starts with "NGuyen" and ends with "sity":
x = re.search("^NGuyen .*sity$", txt)
if (x):
    print("YES! We have a match!")
else:
    print("No match")
# The findall() Function
# The findall() function returns a list containing all matches.

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

x = re.findall("Portugal", txt)
print(x)

txt = "The rain in Spain"
x = re.search("\s", txt)
txt = "The rain in Spain"
y = re.search("Portugal", txt)
print(y)
print("The first white-space character is located in position:", x.start())
x = re.split("\s", txt)
print(x)

x = re.split("\s", txt, 1)
print(x)

# The sub() function replaces the matches with the text of your choice:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# You can control the number of replacements by specifying the count parameter:
x = re.sub("\s", "9", txt, 2)
print(x)

# Match Object
x = re.search("ai", txt)
print(x) #this will print an object


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
x = re.search(r"\bS\w+", txt)
print(x.string)
x = re.search(r"\bS\w+", txt)
print(x.group())

