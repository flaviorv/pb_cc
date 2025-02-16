

def insertion_sort(dll, dnode):
    if dll.head != None and dll.tail!= None:
        current = dll.head
        while current.next != None:
            current = current.next            
            previous = current.previous
            
            if current.value < previous.value:  
                next = current.next
                previous.next = next
            
                if next != None:             
                    next.previous = previous
                else:
                    dll.tail = previous
                    
                previous = previous.previous
                while previous != None and previous.value >= current.value:
                    previous = previous.previous                    
                
                if previous == None:
                    _current = dnode(current.value)
                    dll.insert(_current.value)

                else:
                    _current = dnode(current.value)
                    next = previous.next
                    previous.next = _current
                    _current.next = next
                    next.previous = _current
                    _current.previous = previous




if __name__ == "__main__":

    import sys, os
    q3_2= os.path.abspath(os.path.join(os.path.dirname(__file__), "../q3_2"))
    sys.path.append(q3_2)
    from doubly_linked_list import DLinkedList, DNode
    from random import randrange


    unordered = DLinkedList()
    length = 4
    for i in range(length):
        unordered.append(randrange(0, 100))
    unordered.show("head_to_tail")
    
    insertion_sort(unordered, DNode)
    unordered.show("head_to_tail")
    unordered.show("tail_to_head")
            
            
