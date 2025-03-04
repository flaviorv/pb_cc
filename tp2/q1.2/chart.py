import matplotlib.pyplot as plt
import json

def generate_chart():
    data = None
    with open("./times.json", "r") as f:
        res = json.load(f)
        data = res

    for len in data: 
        title = f"Summing {int(len):,} numbers of a vector"
        names = []
        times = []

        for name in data[len]:
            times.append(data[len][name])
            names.append(name)

        plt.bar(names, times)
        plt.xlabel("Cost of sums and generating lists")
        plt.ylabel("Seconds")
        plt.title(title)
        plt.savefig(f"../data/charts/parallel_sum_s{len}.png")


if __name__ == "__main__":
    generate_chart()