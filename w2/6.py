# comprehension

# for i in range(5):
#   print(i)

# [print(i) for i in range(5)] # [expression for iter in list condition]


a = [i for i in range(10) if i % 2 != 0]

print(a)
print(type(a))
