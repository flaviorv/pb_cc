from rw_files import save, get

def generate_average_time(samples):
    data = get("quick_sort_times.json")

    unordered = {"arr_type": "unordered", "start": 0, "middle": 0, "end": 0, "random": 0}
    ordered = {"arr_type": "ordered", "start": 0, "middle": 0, "end": 0, "random": 0}
    inverse = {"arr_type": "inverse", "start": 0, "middle": 0, "end": 0, "random": 0}

    average_data = [unordered, ordered, inverse]

    for d in data:
        arr_type = d["arr_type"]
        pivot_type = d["pivot_type"]
        sec = d["sec"]
        match(arr_type):
            case "unordered":
                unordered[pivot_type] += sec
            case "ordered":
                ordered[pivot_type] += sec
            case "inverse":
                inverse[pivot_type] += sec

    for a in average_data:
        a["start"] = round(a["start"] / samples, 4)
        a["middle"] = round(a["middle"] / samples, 4)
        a["end"] = round(a["end"] / samples, 4)
        a["random"] = round(a["random"] / samples, 4)

    save(average_data, "quick_sort_average.json")