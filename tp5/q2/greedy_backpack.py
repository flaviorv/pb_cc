
items = [(1, 2, 40), (2, 3, 50), (3, 5, 100), (4, 4, 90)]
capacity = 8

def greedy_backpack(items, capacity):
    print("Greedy Backpack")
    print("Capacity:", capacity)
    print("(Item, Weight, Value)")
    print(items)
    items = sorted(items, key=lambda i:((i[2]/i[1])), reverse=True)
    backpack_weight = 0
    backpack_items = []
    backpack_value = 0
    for item in items:
        if item[1]+backpack_weight <= capacity:
            backpack_weight += item[1]
            backpack_value += item[2]
            backpack_items.append(item[0])
    print("Backpack items:", backpack_items)
    print("Weight:", backpack_weight, "Value:", backpack_value)

if __name__ == "__main__":
    greedy_backpack(items, capacity)