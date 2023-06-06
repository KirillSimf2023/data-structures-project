"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import Node, LinkedList


class TestNode(unittest.TestCase):

    def test_init(self):
        data_1 = Node(5, None)
        self.assertEqual(data_1.data, 5)
        self.assertEqual(data_1.next_node, None)

        data_2 = Node(10, data_1)
        self.assertEqual(data_2.data, 10)
        self.assertEqual(data_2.next_node.data, 5)


class TestNode(unittest.TestCase):

    def test_init(self):
        ll = LinkedList()
        self.assertEqual(ll.tail, None)
        self.assertEqual(ll.head, None)

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.head.next_node, None)
        self.assertEqual(ll.head, ll.tail)
        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.head.data, {'id': 0})
        self.assertEqual(ll.head.next_node.data, {'id': 1})


    def test_insert_at_end(self):
        ll = LinkedList()
        self.assertEqual(ll.tail, None)
        self.assertEqual(ll.head, None)
        ll.insert_at_end({'id': 2})
        self.assertEqual(ll.head, ll.tail)
        self.assertEqual(ll.tail.data, {'id': 2})
        self.assertEqual(ll.tail.next_node, None)
        ll.insert_at_end({'id': 3})
        self.assertEqual(ll.tail.data, {'id': 3})
        self.assertEqual(ll.tail.next_node, None)
        self.assertIsNot(ll.head, ll.tail)
        self.assertEqual(ll.head.next_node.data, {'id': 3})





