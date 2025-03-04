from rw_files import get
import matplotlib.pyplot as plt


def generate_chart():
    data = get("quick_sort_average.json")

    for d in data:
        title = f"Quick sort receiving an {d["arr_type"]} array"
        xlabel = "Type of pivots"
        ylabel = "Seconds"

        pivots = ["start",  "middle", "end", "random"]
        seconds = [d["start"], d["middle"], d["end"], d["random"]]

        plt.bar(pivots, seconds)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.savefig(f"{d["arr_type"]}_times.png")
        plt.savefig(f"../data/charts/quick_sort_with_{d["arr_type"]}.png")

if __name__ == "__main__":
    generate_chart()