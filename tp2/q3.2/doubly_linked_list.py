class DNode:
    def __init__(self, value):
        self.value = value 
        self.previous = None
        self.next = None



class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, value):
        dnode = DNode(value)
        if self.head == None:
            self.head = dnode
            return
        
        next = self.head
        self.head = dnode
        self.head.next = next
        next.previous = self.head
        
        if self.tail == None:
            self.tail = next

    def append(self, value):
        dnode = DNode(value)
        if self.tail == None:
            self.tail = dnode
            return
        
        previous = self.tail
        self.tail = dnode
        self.tail.previous = previous
        previous.next = self.tail
        
        if self.head == None:
            self.head = previous


    def remove(self, position):
        if position == 1 or position == "head":
            new_head = self.head.next
            self.head = new_head
            self.head.previous = None
        
        elif position == -1 or position == "tail":
            new_tail = self.tail.previous
            self.tail = new_tail
            self.tail.next = None

        else:
            if position > 1:
                return self.__remove_head_to_tail(position)        
            elif position < -1:
                return self.__remove_tail_to_head(position)
            
            else:
                return f"Invalid position input ({position})"


    def __remove_head_to_tail(self, position):
        current = self.head.next
        count = 2
        while current != None:
            if count == position:
                next = current.next
                previous = current.previous
                previous.next = next
                next.previous = previous
                return f"Value of position {position} is removed"
            current = current.next
            count += 1
        return f"Position {position} out of range"

    def __remove_tail_to_head(self, position):
        current = self.tail.previous
        count = -2
        while current != None:
            if count == position:
                previous = current.previous
                next = current.next
                previous.next = next
                next.previous = previous
                return f"Value of position {position} is removed"
            current = current.previous
            count -= 1
        return f"Position {position} out of range"

