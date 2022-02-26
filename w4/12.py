import json

with open('data.txt', 'r') as f:
  data = f.read()

a = json.loads(data)
print(type(a))
for obj in a:
  print(obj['id'])
