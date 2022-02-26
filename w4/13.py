import json
game_state = {
    "position": {
        "x": 100,
        "y": 200
    }
}

game_state["full_name"] = "Hello world"
game_state["enemy"] = {
    "x": 200,
    "y": 300
}

with open("output.txt", "w") as f:
  f.write(json.dumps(game_state)) # serializing 

