"""Здесь надо написать тесты с использованием unittest для модуля queue."""

import unittest
from src.queue import Node, Queue

class TestNode(unittest.TestCase):
    def test_init(self):
        data_1 = Node(5, None)
        self.assertEqual(data_1.data, 5)
        self.assertEqual(data_1.next_node, None)

        data_2 = Node('a', data_1)
        self.assertEqual(data_2.data, 'a')
        self.assertEqual(data_2.next_node.data, 5)