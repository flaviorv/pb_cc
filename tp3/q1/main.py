class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__add(self.root, value)

    def __add(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self.__add(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self.__add(current.right, value)

    def in_order(self):
        result = []
        self.__in_order(self.root, result)
        return result

    def __in_order(self, current, result):
        if current is not None:
            self.__in_order(current.left, result)
            result.append(current.value)
            self.__in_order(current.right, result)

    def pre_order(self):
        result = []
        self.__pre_order(self.root, result)
        return result

    def __pre_order(self, current, result):
        if current is not None:
            result.append(current.value)
            self.__pre_order(current.left, result)
            self.__pre_order(current.right, result)

    def post_order(self):
        result = []
        self.__post_order(self.root, result)
        return result

    def __post_order(self, current, result):
        if current is not None:
            self.__post_order(current.left, result)
            self.__post_order(current.right, result)
            result.append(current.value)

    def remove(self, value):
        print(f"Removing {value}...")
        self.root, msg = self.__remove(self.root, value, "not found")
        print(f"{value} {msg}")

    def __remove(self, current, value, msg):
        if current is None:
            return current, msg

        if value < current.value:
            current.left, msg = self.__remove(current.left, value, msg)
        elif value > current.value:
            current.right, msg = self.__remove(current.right, value, msg)
        else:
            msg = "removed"
            if current.left is None and current.right is None:
                return None, msg
            if current.left is None:
                return current.right, msg
            if current.right is None:
                return current.left, msg

            right_sub_min = self.__get_min(current.right)
            current.value = right_sub_min.value
            current.right, msg = self.__remove(current.right, right_sub_min.value, msg)
        return current, msg

    def __get_min(self, current):
        while current.left is not None:
            current = current.left
        return current

    def search(self, value):
        print(f"Searching for {value}...")
        msg = self.__search(self.root, value)
        print(value, msg)

    def __search(self, current, value):
        if current is None:
            return "not found"
        if current.value == value:
            return "found"
        if value < current.value:
            return self.__search(current.left, value)
        else:
            return self.__search(current.right, value)

    def check(self):
        is_bst = self.__check(self.root, True)
        print(f"Is bst: {is_bst}")

    def __check(self, current, is_bst):
        if current != None:
            if current.left is not None and current.left.value > current.value:
                return False
            elif current.right is not None and current.right.value < current.value:
                return False
            else:
                is_bst = self.__check(current.left, is_bst)
                is_bst = self.__check(current.right, is_bst)
        return is_bst

if __name__ == "__main__":
    bs = BinaryTree()
    nodes = [50, 30, 70, 20, 40, 60, 80]
    for node in nodes:
        bs.add(node)
    bs.check()
    print("In order:", bs.in_order())
    print("Pre order:", bs.pre_order())
    print("Post order:", bs.post_order())

    bs.remove(20)
    print("Pre order:", bs.pre_order())
    bs.check()
    bs.remove(30)
    print("Pre order:", bs.pre_order())
    bs.check()
    bs.remove(50)
    print("Pre order:", bs.pre_order())
    bs.check()

    bs.search(40)
    bs.search(50)

    bs.root.left.left = Node(100)
    bs.check()



