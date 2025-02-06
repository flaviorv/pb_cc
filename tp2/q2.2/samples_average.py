from rw_files import get, save

def generate_average_time(samples):
    starts = 0
    middles = 0
    ends = 0
    randoms = 0

    data = get("quick_sort_times.json")
   
    for d in data:
        pivot_type = d["pivot_type"]
        match(pivot_type):
            case "start":
                starts += d["sec"]
            case "middle":
                middles += d["sec"]                   
            case "end":
                ends += d["sec"]
            case "random":
                randoms += d["sec"]

    start_average = {"pivot_type": "start", "sec": (starts / samples)}
    middle_average = {"pivot_type": "middle", "sec": middles / samples}
    end_average = {"pivot_type": "end", "sec": ends / samples}
    random_average = {"pivot_type": "random", "sec": randoms / samples}


    save([start_average, middle_average, end_average, random_average], "quick_sort_average.json")
        
generate_average_time(3)
