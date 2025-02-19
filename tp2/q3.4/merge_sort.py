import sys, os
q3_2= os.path.abspath(os.path.join(os.path.dirname(__file__), "../q3.2"))
sys.path.append(q3_2)
from doubly_linked_list import DLinkedList

def merge(sorted_dll1, sorted_dll2):
    dll1_node = sorted_dll1.head
    dll2_node = sorted_dll2.head

    if (dll1_node == None):
        if(sorted_dll1.tail == None):
            return "Doubly linked list 1 is empty"
        dll1_node = sorted_dll1.tail

    if (dll2_node == None):
        if(sorted_dll2.tail == None):
            return "Doubly linked list 2 is empty"
        dll2_node = sorted_dll2.tail

    merged_dll = DLinkedList()
    while dll1_node != None and dll2_node != None:
        if dll1_node.value <= dll2_node.value:
            merged_dll.append(dll1_node.value)
            dll1_node = dll1_node.next
        else:
            merged_dll.append(dll2_node.value)
            dll2_node = dll2_node.next


    while dll1_node != None:
        merged_dll.append(dll1_node.value)
        dll1_node = dll1_node.next
    
    while dll2_node != None:
        merged_dll.append(dll2_node.value)
        dll2_node = dll2_node.next

    return merged_dll    

