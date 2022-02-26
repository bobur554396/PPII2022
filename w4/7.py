# Scope 
b = 10  # Global scope variable

def hello():
  x = 2  # Local scope variable
  # b = 11 # local variable
  global b
  b = b + 5
  print(b)

  def hi():
    print(x)
  hi()

# print(x) # x is not defined here


hello()
# print(b)
