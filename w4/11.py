# What is JSON - JavaScript Object Notation 
import json

a = {
  'id': '123',
  'name': 'KBTU',
  'location': 'Tole bi 59'
}

b = json.dumps(a) # converting dict -> string | serializing data to string
# print(b)

c = json.loads(b)  # converting string -> dict | deserializing data to dict
print(type(c))
print(c['id'])

