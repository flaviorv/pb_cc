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

def __search(root, value, result):
    if root is None:
        result.put(False)
        return

    if root.value == value:
        result.put(True)
        return

    stack = [root]
    while stack:
        node = stack.pop()
        if node.value == value:
            result.put(True)
            return
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    result.put(False)

def parallel_search(root, value):
    result = multiprocessing.Queue()
    if root.value == value:
        return True

    left_process = multiprocessing.Process(target=__search, args=(root.left, value, result))
    right_process = multiprocessing.Process(target=__search, args=(root.right, value, result))
    left_process.start()
    right_process.start()
    left_process.join()
    right_process.join()

    while not result.empty():
        if result.get():
            return True
    return False

def __parallel_dfs(root, value, queue):
    if root is None:
        queue.put(None)
        return

    if root.value == value:
        queue.put([root.value])
        return

    left_queue = multiprocessing.Queue()
    right_queue = multiprocessing.Queue()
    left_process = right_process = None
    if root.left:
        left_process = multiprocessing.Process(target=__dfs_path, args=(root.left, value, left_queue))
        left_process.start()
    if root.right:
        right_process = multiprocessing.Process(target=__dfs_path, args=(root.right, value, right_queue))
        right_process.start()

    left_path = right_path = None
    if left_process:
        left_process.join()
        left_path = left_queue.get()
    if right_process:
        right_process.join()
        right_path = right_queue.get()

    if left_path:
        queue.put([root.value] + left_path)
    elif right_path:
        queue.put([root.value] + right_path)
    else:
        queue.put(None)

def __dfs_path(root, value, queue):
    stack = [(root, [])] if root else []
    while stack:
        node, path = stack.pop()
        if node:
            new_path = path + [node.value]
            if node.value == value:
                queue.put(new_path)
                return

            if node.right:
                stack.append((node.right, new_path))
            if node.left:
                stack.append((node.left, new_path))

    queue.put(None)

def dfs_path(root, target):
    queue = multiprocessing.Queue()
    __parallel_dfs(root, target, queue)
    return queue.get()

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
       # print(f"\33[32m{n} found\33[0m") if parallel_search(root, n) else print(f"\33[31m{n} not found\33[0m")

        path = dfs_path(root, n)
        print(f"\33[32mUntil {n}: {path}\33[0m") if path else print(f"\33[31m{n} not found\33[0m")


if __name__ == "__main__":
    main()
