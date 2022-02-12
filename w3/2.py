def hello(name):
  print(f'hi {name}')

# hello('FIT')

def sum(a, b):
  # print(a + b)
  return a + b

# c = sum(2, 3)
# print(c)

def sum(a: int, b: int) -> float:
  return float(a + b)

c = sum('2', '3')
print(c)
