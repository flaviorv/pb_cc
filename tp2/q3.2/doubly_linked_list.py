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
            if self.head != None:
                self.head.previous = None
            
        elif position == -1 or position == "tail":
            new_tail = self.tail.previous
            self.tail = new_tail
            if self.tail != None:
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


    def show(self, direction):
        if direction == "head_to_tail":
            self.__show_head_to_tail()
        elif direction == "tail_to_head":
            self.__show_tail_to_head()
        else:
            print("Invalid direction")
            
        

    def __show_head_to_tail(self):
        if self.tail == None and self.head == None:
            print(f"\33[1m\33[34mEmpty list\33[0m")
        elif self.head != None and self.tail == None:
            print(f"\33[1m\33[34m{self.head.value}\33[0m")
        elif self.head == None and self.tail!= None:
            print(f"\33[1m\33[34m{self.tail.value}\33[0m")
        else:
            current = self.head
            while current.next != None:
                print(f"\33[1m\33[34m{current.value}", end="->\33[0m")
                current = current.next
            print(f"\33[1m\33[34m{self.tail.value}\33[0m")
    

    def __show_tail_to_head(self):
        if self.tail == None and self.head == None:
            print(f"\33[1m\33[34mEmpty list\33[0m")
        elif self.head != None and self.tail == None:
            print(f"\33[1m\33[34m{self.head.value}\33[0m")
        elif self.head == None and self.tail!= None:
            print(f"\33[1m\33[34m{self.tail.value}\33[0m")
        else:
            current = self.tail
            while current.previous != None:
                print(f"\33[1m\33[34m{current.value}", end="->\33[0m")
                current = current.previous
            print(f"\33[1m\33[34m{self.head.value}\33[0m")

