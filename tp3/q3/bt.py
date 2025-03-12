import multiprocessing
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def add(root, values):
    return __add(values, 0, len(values) - 1)

def __add(values, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = Node(values[mid])

    root.left = __add(values, start, mid - 1)
    root.right = __add(values, mid + 1, end)
    return root

def __search(root, target, result):
    if root is None:
        result.put(False)
        return

    if root.value == target:
        result.put(True)
        return

    stack = [root]
    while stack:
        node = stack.pop()
        if node.value == target:
            result.put(True)
            return
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    result.put(False)

def parallel_search(root, target):
    result = multiprocessing.Queue()
    if root.value == target:
        return True

    left_process = multiprocessing.Process(target=__search, args=(root.left, target, result))
    right_process = multiprocessing.Process(target=__search, args=(root.right, target, result))
    left_process.start()
    right_process.start()
    left_process.join()
    right_process.join()

    while not result.empty():
        if result.get():
            return True
    return False

def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.value, end=" ")
        print_tree(root.right)

def main():
    root = Node(random.randrange(1, 101))
    random_values = [random.randrange(1, 101) for _ in range(20)]
    root = add(root, random_values)
    print("Tree elements:")
    print_tree(root)
    print()
    print("Search:")
    for _ in range(20):
        n = random.randrange(1, 101)
        print(f"\33[32m{n} found\33[0m") if parallel_search(root, n) else print(f"\33[31m{n} not found\33[0m")

if __name__ == "__main__":
    main()
