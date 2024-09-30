import json
with open("./Autonomie/user.json", "r") as f:
    data = json.load(f)

print(data['age'])
print(data['hobbies'][1])
print(data['email'])
