a = [1, 2, 3]
# b = a
b = a.copy()

b.append(4)
a.append(5)

print('a =', a)
print('b =', b)


print(hex(id(a)))
print(hex(id(b)))
