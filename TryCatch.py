try:
    print(x)
except:
    print("An exception occurred")
    x = -1

    if x < 0:
        raise Exception("Sorry, no numbers below zero")

    x = "hello"
    if not type(x) is int:
        raise TypeError("Only integers are allowed")

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


