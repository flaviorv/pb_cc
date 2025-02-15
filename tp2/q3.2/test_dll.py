import unittest
import doubly_linked_list

class TestDLinkedList(unittest.TestCase):
    
    def test_is_node(self):
        dll = doubly_linked_list.DLinkedList()
        dll.insert(10)
        self.assertTrue(isinstance(dll.head, doubly_linked_list.DNode))
        self.assertEqual(dll.head.next, None)
        self.assertEqual(dll.head.previous, None)
    
    def test_insert(self):
        dll = doubly_linked_list.DLinkedList()
        dll.insert(10)
        dll.insert(20)
        self.assertEqual(dll.head.value, 20)
        self.assertEqual(dll.tail.value, 10)
        dll.insert(30)
        dll.insert(40)
        self.assertEqual(dll.head.value, 40)
        self.assertEqual(dll.tail.value, 10)
        self.assertEqual(dll.head.next.value, 30)
        self.assertEqual(dll.head.next.previous.value, 40)
        self.assertEqual(dll.head.next.next.next.value, 10)
        self.assertEqual(dll.tail.previous.previous.previous.value, 40)
        
    def test_append(self):
        dll = doubly_linked_list.DLinkedList()
        dll.append(10)
        dll.append(20)
        self.assertEqual(dll.head.value, 10)
        self.assertEqual(dll.tail.value, 20)
        dll.append(30)
        dll.append(40)
        self.assertEqual(dll.head.value, 10)
        self.assertEqual(dll.tail.value, 40)
        self.assertEqual(dll.tail.previous.value, 30)
        self.assertEqual(dll.tail.previous.next.value, 40)
        self.assertEqual(dll.head.next.next.next.value, 40)
        self.assertEqual(dll.tail.previous.previous.previous.value, 10)

    def test_remove(self):
        dll = doubly_linked_list.DLinkedList()
        dll.append(10)
        dll.append(20)
        dll.append(30)
        dll.append(40)
        dll.append(50)
        dll.append(60)
        dll.append(70)
        dll.append(80)
        dll.append(90)
        dll.append(100)

        dll.remove(1)
        self.assertEqual(dll.head.value, 20)
        self.assertEqual(dll.head.previous, None)
        self.assertEqual(dll.head.next.value, 30)

        dll.remove(-1)
        self.assertEqual(dll.tail.value, 90)
        self.assertEqual(dll.tail.previous.value, 80)
        self.assertEqual(dll.tail.next, None)

        dll.remove(-3)
        self.assertEqual(dll.tail.value, 90)
        self.assertEqual(dll.tail.previous.value, 80)
        self.assertEqual(dll.tail.previous.previous.value, 60)
        self.assertEqual(dll.tail.previous.previous.previous.value, 50)

        dll.remove(-2)
        self.assertEqual(dll.tail.previous.previous.value, 50)
        self.assertEqual(dll.tail.previous.next.value, 90)

        dll.remove(2)
        self.assertEqual(dll.head.next.previous.value, 20)
        self.assertEqual(dll.head.next.next.value, 50)

        
        self.assertEqual(dll.remove(10), "Position 10 out of range")
        self.assertEqual(dll.remove(0), "Invalid position input (0)")
        self.assertEqual(dll.remove(-10), "Position -10 out of range")



if __name__ == "__main__":
    unittest.main()