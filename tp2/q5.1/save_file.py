import json

def save(content):
    with open("./times.json", "w") as f:
        json_content = json.dumps(content, indent=2)
        f.write(json_content)