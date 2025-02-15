import unittest
import singly_linked_list

class TestSinglyLinkedList(unittest.TestCase):
    def test_append(self):
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


if __name__ == "__main__":
    unittest.main()