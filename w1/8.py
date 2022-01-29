x = "awesome"

def myfunc(): # new scope
  global x
  x = "fantastic"
  # print("Python is " + x)


myfunc()

print("Python is " + x)
