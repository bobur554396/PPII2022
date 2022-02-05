# a = tuple((1, 2, 3))
a = tuple((1, 2, 3, 4, 5, 6, 7))

# n1, n2, n3 = a
n1, *n2 = a


print(n1)
print(n2)
# print(n3)
