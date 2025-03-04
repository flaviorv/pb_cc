import matplotlib.pyplot as plt
import json

def get_data():
    with open("times.json", "r") as f:
        json_content = f.read()
        content = json.loads(json_content)
        return content


def get_arranged_data():
    times = []
    discs = []
    content = get_data()
    for c in content:
        times.append(c["time"])
        discs.append(c["discs"])
    return [discs, times]


def generate_chart():
    data = get_arranged_data()
    plt.plot(data[0], data[1])
    plt.title("Torre de Hanói - Tempo exponencial - O(2ⁿ)")
    plt.xlabel("Discos")
    plt.ylabel("Segundos")
    plt.savefig("../data/charts/hanoi.png")



if __name__ == "__main__":
    generate_chart()