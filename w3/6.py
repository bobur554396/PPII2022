def f1(x):
  return x

# print(f1(10))

# lambda arguments : expression
f2 = lambda x: x
# print(f2(10))

square = lambda x: x * x
# print(square(4))

sum = lambda a, b: a + b

# print(sum(2, 3))

a = [1, 2, 3, 4, 5, 6]
def double_it(x):
  return x * 2

# map(function, iterable_object)
# filter(function, iterable_object)
# arr = list(map(double_it, a))

# arr = list(map(lambda x: x * 2, a))

arr = list(filter(lambda x: x % 2 != 0, a))

# print(arr)



def multiplier(n):
  return lambda x: x * n

doubler = multiplier(2)
# print(doubler(100))

tripler = multiplier(3)
print(tripler(5))
