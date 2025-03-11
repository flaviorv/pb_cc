class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    

    def add(self, value):
        if self.root == None:
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

if __name__ == "__main__":
    bs = BinaryTree()
    nodes = [50, 30, 70, 20, 40, 60, 80]
    for node in nodes:
        bs.add(node)
    
    print(bs.in_order())
    print(bs.pre_order())
    print(bs.post_order())
