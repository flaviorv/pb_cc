import json

def save(data, file):
    with open(file, "w") as f:
        json_data = json.dumps(data, indent=2)
        f.write(json_data)

def get(file):
    with open(file, "r") as f:
        data = json.load(f)
        return data
        