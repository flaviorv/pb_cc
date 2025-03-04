import unittest
import singly_linked_list

class TestSinglyLinkedList(unittest.TestCase):
    def test_append(self):
        print("SINGLY LINKED LIST TESTS")
        print("Append test")
        sll = singly_linked_list.LinkedList()
        sll.append(10)
        self.assertEqual(sll.head.value, 10)
        self.assertEqual(sll.head.next, None)

        sll.append(20)
        self.assertEqual(sll.head.value, 10)
        self.assertEqual(sll.head.next.value, 20)
        self.assertEqual(sll.head.next.next, None)
        
        sll.append(30)
        self.assertEqual(sll.head.value, 10)
        self.assertEqual(sll.head.next.next.value, 30)
        self.assertEqual(sll.head.next.next.next, None)

    def test_insert(self):
        print("Insert test")
        sll = singly_linked_list.LinkedList()
        sll.insert(10)
        self.assertEqual(sll.head.value, 10)
        self.assertEqual(sll.head.next, None)

        sll.insert(20)
        self.assertEqual(sll.head.value, 20)
        self.assertEqual(sll.head.next.value, 10)
        self.assertEqual(sll.head.next.next, None)
        
        sll.insert(30)
        self.assertEqual(sll.head.value, 30)
        self.assertEqual(sll.head.next.next.value, 10)
        self.assertEqual(sll.head.next.next.next, None)

    
    def test_remove(self):
        print("Remove test")
        sll = singly_linked_list.LinkedList()
        sll.append(10)
        sll.append(20)
        sll.append(30)
        sll.append(40)
        sll.append(50)
        
        sll.remove(20)
        self.assertEqual(sll.head.next.value, 30)
        sll.remove(40)
        self.assertEqual(sll.head.next.next.value, 50)
        sll.remove(10)
        self.assertEqual(sll.head.value, 30)
        sll.remove(50)
        self.assertEqual(sll.head.value, 30)
        sll.remove(30)
        self.assertEqual(sll.head, None)


    def test_search(self):
        print("Search test")
        sll = singly_linked_list.LinkedList()
        
        self.assertEqual(sll.search(0), "Empty list")

        sll.append(10)
        sll.append(20)
        sll.append(30)
        sll.append(40)
        sll.append(50)

        self.assertEqual(sll.search(10), {"index": 0, "value": 10})
        self.assertEqual(sll.search(20), {"index": 1, "value": 20})
        self.assertEqual(sll.search(30), {"index": 2, "value": 30})
        self.assertEqual(sll.search(50), {"index": 4, "value": 50})
        self.assertEqual(sll.search(0), "Node not found")
    
    def test_invert(self):
        print("Invert test")
        sll = singly_linked_list.LinkedList()
        sll.append(10)
        sll.append(20)
        sll.append(30)
        sll.append(40)
        sll.append(50)
        sll.show()
        print("Inverting...")
        sll.invert()

    def test_invert_with_one_element(self):
        print("Invert one element test")
        sll = singly_linked_list.LinkedList()
        self.assertEqual(sll.invert(), "Empty list")
        sll.append(10)
        sll.invert()
    
    def test_invert_with_two_elements(self):
        print("Invert two elements test")
        sll = singly_linked_list.LinkedList()
        self.assertEqual(sll.invert(), "Empty list")
        sll.append(10)
        sll.invert()
        sll.append(20)
        sll.invert()


if __name__ == "__main__":
    unittest.main()