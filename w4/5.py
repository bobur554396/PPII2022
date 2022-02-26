# a = [1, 2, 3]
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n
    n += 1
    print('This is printed second')
    yield n
    n += 1
    print('This is printed at last')
    yield n


# a = my_gen()
# print(next(a))
# print(next(a))
# print(next(a))

for item in my_gen():
    print(item)
