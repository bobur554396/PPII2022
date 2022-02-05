# int[] a;
# a = [1, 2, 3, 4]
a = [1, 2, 'hello', True, {'id': '20B123123', 'name': 'Student 1', 'gpa': 4.0}]
# a = list((1, 2, 'hello', True, {'id': '20B123123', 'name': 'Student 1', 'gpa': 4.0}))

print(len(a))
print(type(a))

# print(a[2:])
# print(a[:3])


# 1)
# ok = False
# for i in a:
#   if isinstance(i, int) and i == 2:
#     ok = True
#     break

# if ok:
#   print('yes')
# else:
#   print('no')


# 2)
if 'hello2' in a:
  print('yes')
else:
  print('no')
