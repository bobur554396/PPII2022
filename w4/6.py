a = int(input('Give amount: '))

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# print(list(fib(a)))

for i in fib(a):
  print(i)

# a = fib(10)
# next(a)
# next(a)
