from linked_list import *
import unittest
class LinkedListTest(unittest.TestCase):

    def test_add(self):
        list = LinkedList()
        list.add_first(1)
        self.assertEqual(list.first.item, 1)
        self.assertEqual(list.last, list.first)
        self.assertIsNone(list.first.next)
        self.assertIsNone(list.first.prev, None)
        list.add_first(0)
        self.assertIsNone(list.first.prev)
        self.assertEqual(list.last, list.first.next)
        self.assertEqual(list.first.item, 0)
        self.assertEqual(list.last.item, 1)
        self.assertEqual(list.last.prev, list.first)

    def test_remove(self):
        list = LinkedList()
        list.add_first(0)
        list.add_last(1)
        list.add_last(2)
        list.remove_last()
        self.assertEqual(list.last.item, 1)
        self.assertIsNone(list.last.next)
        list.remove_first()
        self.assertEqual(list.first, list.last)
        self.assertEqual(list.first.item, 1)
        self.assertIsNone(list.first.next)
        self.assertIsNone(list.first.prev)

if __name__ == '__main__':
    unittest.main()
