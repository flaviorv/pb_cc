import requests
from urls import urls
import time
import os
import json

def sequential_drink_requests():
    for url in urls:
        response = requests.get(url)
        data = response.json()
        if data["drinks"] != None:
            drink_name = data["drinks"][0]["strDrink"]
            print(drink_name)

def save_time(time_data):
    path = f"./times/sequential.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        time_data = json.dumps(time_data, indent=2)
        f.write(time_data)


if __name__ == "__main__":
    start = time.time()
    sequential_drink_requests()
    end = time.time()
    total_time = round((end-start), 2)
    print("Sequential: {} seconds".format(total_time))
    time_data = {"threads": None, "seconds":total_time}
    save_time(time_data)