import matplotlib.pyplot as plt
import json

def create_chart():
    data = None
    with open("./times.json", "r") as f:
        data = json.load(f)

    times = []
    threads = [] 
    for d in data:
        threads.append(d["threads"])
        times.append(d["seconds"])

    plt.plot(threads, times)
    plt.xlabel("Threads")
    plt.ylabel("Seconds")
    plt.title("Runtime of image filter applying")
    plt.savefig("../data/charts/imgs_edting.png")


if __name__ == "__main__":
    create_chart()