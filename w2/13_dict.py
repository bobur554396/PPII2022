# a = {
#   'id': '21B123123',
#   'name': 'Student 1',
#   'age': 18,
#   'gpa': 4.0
# }

a = dict(id='21B123123', name='Student 1', age=18, gpa=4.0)


del a['age']

a.pop('id')

print(len(a))
print(type(a))

print(a.keys())
print(a.values())
print(a.items())

for key, value in a.items():
  print(f'{key} ---> {value}')
