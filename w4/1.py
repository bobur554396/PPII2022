# What is an Iterator?
# Iterable objects - List, Tuple, Set, Dict

list1 = [10, 5, 23, 6, 12]

it = iter(list1)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# for i in list1:
#   print(i)