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

   
