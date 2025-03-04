import sys, os
q3_2= os.path.abspath(os.path.join(os.path.dirname(__file__), "../q3.2"))
sys.path.append(q3_2)
from doubly_linked_list import DLinkedList, DNode
from insertion_sort import insertion_sort
from random import randrange
import unittest


class InsertionSortTest(unittest.TestCase):
    def test(self):
        print("Testing if the sorting works")
        samples = 10
        for i in range(samples):
            dll = DLinkedList()
            length = i+1
            checklist = []
            for _ in range(length):
                num = randrange(0, 100)
                dll.append(num)
                checklist.append(num)

            print("Unordered:")
            print("Head to tail: ", end="")
            dll.show("head_to_tail")
            print("Checklist:", checklist)
            insertion_sort(dll, DNode)
            checklist.sort()
            
            
            if dll.head != None:
                current = dll.head
            else:
                current = dll.tail

            for i in range(length):
                self.assertEqual(current.value, checklist[i])
                current = current.next
            
            print("Sorted:")
            print("Head to tail: ", end="")
            dll.show("head_to_tail")
            print("Tail to head: ", end="")
            dll.show("tail_to_head")
            print("Checklist:", checklist, end="\n\n")


if __name__ == "__main__":
    unittest.main()