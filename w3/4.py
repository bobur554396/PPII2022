def fun1(a, b):
  print(a, b)

# fun1(2, 'hello', 'hi')

# a, b, *c = (1, 2, 3, 4, 5)
# print(a)
# print(b)
# print(c)

def fun2(*args):
  # print(type(args))
  for arg in args:
    print(arg)

# fun2(1, 'hello', 'hi', True, {'name': 'Student1'}, [1, 2, 4, 5])


def fun3(a, b, *args): # args => arguments -> tuple
  print(a)
  print(b)
  print(args)


# fun3(1, 'hello', 'hi', True, {'name': 'Student1'}, [1, 2, 4, 5])


def fun4(id, name):
  print(id)
  print(name)


# fun4(name='Student1', id='21B12312')

def fun5(id, name, **kwargs): # kwargs => key word arguments => dict
  print(id)
  print(name)
  
  for (key, val) in kwargs.items():
    print(f'{key} ---> {val}')


# fun5(id='21B12312', name='Student1', gpa=4.0, year=2, age=20)


# a = dict(id='21B12312', name='Student1', gpa=4.0, year=2, age=20)
# for (key, value) in a.items():
#   print(f'{key} --> {value}')


'''
2 3
5
'''
nums = list(map(int, input().split()))

# print(sum(nums))

def sum(*nums):
  s = 0
  for i in nums:
    s += i
  return s
