# Generator ?

# a = [1, 2, 3, 4]

def gen():
  yield 1
  yield 2
  yield 3
  
a = gen()
# print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
