# Generator ?

# a = [1, 2, 3, 4]

from turtle import ycor


def gen():
  print('asdasd')
  print('asdasd')
  print('asdasd')
  print('asdasd')
  print('asdasd')
  yield 1
  
  print('asdasd')
  print('asdasd')
  print('asdasd')
  print('asdasd')
  print('asdasd')
  yield 2
  
  print('asdasd')
  print('asdasd')
  print('asdasd')
  yield 3

def users_gen():
  for i in range(100000):
    yield i

# users = [1, 2, 3, 4, .... 20bln]
users = users_gen()

for user in users:
  print(user)
  
a = gen()
# print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
