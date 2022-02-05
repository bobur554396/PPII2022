a = {1, 1, 2, 3}
# a = set()

a.add(1)
a.add(1)
a.add(1)
a.add(2)

a.remove(1)

print(len(a))
print(a)
print(type(a))

print(2 in a)

for i in a:
  print(i)


