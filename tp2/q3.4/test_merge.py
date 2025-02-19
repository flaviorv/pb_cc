import unittest
from merge_sort import merge, DLinkedList

class Test(unittest.TestCase):
    
    def test_empty_dll(self):
        dll1 = DLinkedList()
        dll2 = DLinkedList()
        dll2.insert(10)

        self.assertEqual(merge(dll1, dll2), "Doubly linked list 1 is empty")

        dll1.insert(10)
        dll2.remove(1)

        self.assertEqual(merge(dll1, dll2), "Doubly linked list 2 is empty")


    def test_many_nodes(self):
        dll1 = DLinkedList()
        dll2 = DLinkedList()

        checklist = []

        for i in range(1, 11):
            dll1.append(i+5)
            dll2.append(i)
            checklist.append(i)
            checklist.append(i+5)

        print("Dll1", end=" ")
        dll1.show("head_to_tail")
        print("Dll2", end=" ")
        dll2.show("head_to_tail")

        merged_dll = merge(dll1, dll2)

        print("Merged", end=" ")
        merged_dll.show("head_to_tail")

        current = merged_dll.head
        checklist.sort()
        for i in range(len(checklist)):
            self.assertEqual(current.value, checklist[i])
            if (current.next != None and i == len(checklist)-1) or (current.next == None and i != len(checklist)-1):
                raise Exception("The lists length is different")
            current = current.next


    def test_two_nodes(self):
        dll1 = DLinkedList()
        dll2 = DLinkedList()
        dll1.insert(20)
        dll2.append(10)

        print("Dll1", end=" ")
        dll1.show("head_to_tail")
        print("Dll2", end=" ")
        dll2.show("head_to_tail")

        merged_dll = merge(dll1, dll2)

        print("Merged", end=" ")
        merged_dll.show("head_to_tail")

        self.assertEqual(merged_dll.head.value, 10)
        self.assertEqual(merged_dll.tail.value, 20)

        merged_dll = merge(dll2, dll1)

        self.assertEqual(merged_dll.head.value, 10)
        self.assertEqual(merged_dll.tail.value, 20)
        


if __name__ == "__main__":
    unittest.main()

        