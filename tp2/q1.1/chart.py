import matplotlib.pyplot as plt
import os
import json

files = []
dir = "./times"
def __get_files(dir):
    try:
        with os.scandir(dir) as directory:
            for content in directory:
                if content.is_file(follow_symlinks=False):
                    files.append(content.name)
                    print(content.name)
    except PermissionError:
        print(f"Access denied")

threads = []
times = []
def __fill():
    for file in files:
        with open(f"{dir}/{file}", "r") as f:
            data = json.load(f)
            thr = data['threads']
            if thr == None:
                thr = "Sequential"
            threads.append(str(thr))
            times.append(data['seconds'])


def __spawn_chart():
    sorted_pairs = sorted(zip(times, threads))
    _times, _threads = zip(*sorted_pairs)
    plt.bar(_threads, _times)
    plt.xlabel("Threads")
    plt.ylabel("Seconds")
    plt.title("Execution Time of HTTP Requests")
    plt.savefig("../data/charts/http_requests.png")
    print("feito")

def spawn_chart():
    __get_files(dir)
    __fill()
    __spawn_chart()

