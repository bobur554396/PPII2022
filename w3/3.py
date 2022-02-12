# Global scope
b = 3 # Global variable


def square(n): # function scope 
  res = n * n # local variable
  res = res + b
  return res

def mult(a, b):
  c = a * b # Local variable
  return c

# print(res)

print(square(4))
