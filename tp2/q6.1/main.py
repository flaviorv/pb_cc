from random import randrange

n_items = 6
capacity = 9
items = [{"weight":randrange(1, capacity+3), "value":randrange(1, 15)} for _ in range(n_items)]

def show_items(items):
    total_weight = 0
    total_value = 0
    for item in items:
        w = item['weight']
        v = item['value']
        print(f"W {w} V{v}")
        total_value += v
        total_weight+= w
    print(f"Capacity = {capacity}")
    print(f"Result = W {total_weight} V{total_value}")


def knapsack_dynamic(items, capacity):
    # this is a pseudo-polynomial time - O(nW) - n is the number of items and W is the capacity of the knapsack
    items_len = len(items)
    table = [[0 for _ in range(capacity + 1)] for _ in range(items_len+1)]

    for item in range(items_len+1):
        for weight in range(capacity + 1):
            if item == 0 or weight == 0:
                table[item][weight] = 0
            elif items[item-1]['weight'] <= weight:
                table[item][weight] = max(items[item-1]['value'] + table[item-1][weight-items[item-1]['weight']], table[item-1][weight])   
            else:
                table[item][weight] = table[item-1][weight]

    weight = capacity
    chosen_items = []

    for item in range(items_len, 0, -1):
        if table[item][weight] != table[item-1][weight]:
            chosen_items.append(items[item-1])
            weight -= items[item-1]['weight']

    return chosen_items

print("All items:")
show_items(items)
print("----------------------------")
print("Best combination:")
show_items(knapsack_dynamic(items, capacity))