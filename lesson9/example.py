import json
data = {"name": "Василий",
        "surname": "Петров",
        "address": {"city": "Hollywood", "street": "New"}
        }
with open("data.json", "w") as outfile:
    json.dump(data, outfile)

with open("data.json", "r") as f:
    data2 = json.loads(f.read())
print(data2)