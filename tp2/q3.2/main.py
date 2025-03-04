import unittest
import doubly_linked_list

class TestDLinkedList(unittest.TestCase):
    print("DOUBLY LINKED LIST TESTS")
    def test_is_node(self):
        print("Is node test")
        dll = doubly_linked_list.DLinkedList()
        dll.insert(10)
        self.assertTrue(isinstance(dll.head, doubly_linked_list.DNode))
        self.assertEqual(dll.head.next, None)
        self.assertEqual(dll.head.previous, None)
    
    def test_insert(self):
        print("Insert test")
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
        print("Append test")
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

    def append_and_insert(self):
        print("Append and insert test")
        dll = doubly_linked_list.DLinkedList()
        dll.append(10)
        dll.insert(20)
        self.assertEqual(dll.tail.value, 10)
        self.assertEqual(dll.head.value, 20)
        self.assertEqual(dll.head.next.value, 10)
        self.assertEqual(dll.tail.previous.value, 20)

    def insert_and_append(self):
        print("Insert and append test")
        dll = doubly_linked_list.DLinkedList()
        dll.insert(20)
        dll.append(10)
        self.assertEqual(dll.tail.value, 10)
        self.assertEqual(dll.head.value, 20)
        self.assertEqual(dll.head.next.value, 10)
        self.assertEqual(dll.tail.previous.value, 20)
        


    def test_remove(self):
        print("Remove test")
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


    def test_show_head_to_tail_with_append(self):
        print("Test of show head to tail test wit append")
        dll = doubly_linked_list.DLinkedList()
        dll.show("anything")
        dll.show("head_to_tail")
        dll.append(10)
        dll.show("head_to_tail")
        dll.append(20)
        dll.append(30)
        dll.append(40)
        dll.append(50)
        dll.show("head_to_tail")

    def test_show_tail_to_head_with_append(self):
        print("Test of show tail to head with append")
        dll = doubly_linked_list.DLinkedList()
        dll.show("anything")
        dll.show("tail_to_head")
        dll.append(10)
        dll.show("tail_to_head")
        dll.append(20)
        dll.append(30)
        dll.append(40)
        dll.append(50)
        dll.show("tail_to_head")


    def test_show_tail_to_head_with_insert(self):
        print("Test of show tail to head with insert")
        dll = doubly_linked_list.DLinkedList()
        dll.show("tail_to_head")
        dll.insert(10)
        dll.show("tail_to_head")
        dll.insert(20)
        dll.insert(30)
        dll.insert(40)
        dll.insert(50)
        dll.show("tail_to_head")

    def test_show_head_to_tail_with_insert(self):
        print("Test of show head to tail with insert")
        dll = doubly_linked_list.DLinkedList()
        dll.show("head_to_tail")
        dll.insert(10)
        dll.show("head_to_tail")
        dll.insert(20)
        dll.insert(30)
        dll.insert(40)
        dll.insert(50)
        dll.show("head_to_tail")

if __name__ == "__main__":
    unittest.main()