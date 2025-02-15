class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            print(f"\33[32mValue {value} was set as head\33[0m", end=" ")
            self.show()
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = node
        print(f"\33[32mValue {value} was appended at the end\33[0m", end=" ")
        self.show()
    

    def insert(self, value):
        node = Node(value)
        old = self.head
        self.head = node
        node.next = old
        print(f"\33[32mValue {value} was iserted at the begining\33[0m", end=" ")
        self.show()


    def remove(self, value):
        current = self.head
        if not current:
            print("\33[31mNo values in the linked list\33[0m", end=" ")
            self.show()
            return
        
        if current.value == value:
            print(f"\33[31mHead {current.value} was removed\33[0m", end=" ")
            self.head = self.head.next
            self.show()
            return
        
        while current:
            previous = current
            current = current.next
            if current:
                if current.value == value:
                    print(f"\33[31mValue {current.value} was removed\33[0m", end=" ")
                    previous.next = current.next
                    self.show()
                    return
            else:
                print(f"\33[31mValue {value} not found to be removed\33[0m", end=" ")
                self.show()


    def show(self):
        if not self.head:
            print(f"\33[1m\33[30mNo nodes\33[0m")

        _current = self.head
        while _current:  
            if _current.next:
                print(f"\33[1m\33[30m{_current.value}", end="->")
            else:
                print(f"\33[1m\33[30m{_current.value}\33[0m")
            
            _current = _current.next


    def search(self, value):
        if self.head == None:
            return "Empty list"

        current = self.head
        count = 0
        while current != None:
            if value == current.value:
                return {"index": count, "value": value}
            count += 1
            current = current.next
        
        return "Node not found"
            

    def invert(self):
        current = self.head
        if self.head != None:
            inverted = LinkedList()
            while current != None:
                inverted.insert(current.value)
                current = current.next
            inverted.show()
        else:
            return "Empty list"
        