from time import time
from hanoi_tower import init
import json

def __get_time(discs):
    start = round(time(), 3)
    init(discs)
    end = round(time(), 3)
    t = round(end - start , 3) 
    return {"discs": discs, "movements": (2**discs -1), "time": t}


def save_times(discs_sequence):
    times = []
    for disc in range(1, discs_sequence+1):
        times.append(__get_time(disc))
    
    content = json.dumps(times, indent=2)
    with open("times.json", "w") as f:
        f.write(content)
        