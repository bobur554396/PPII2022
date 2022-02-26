import json

with open('output.txt', 'r') as f:
  game_state = json.loads(f.read()) # deserializing
  

print(game_state)