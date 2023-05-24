"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack

class TestNode(unittest.TestCase):
    def test_init(self):
        data_1 = Node(5, None)
        self.assertEqual(data_1.data, 5)
        self.assertEqual(data_1.next_node, None)

        data_2 = Node('a', data_1)
        self.assertEqual(data_2.data, 'a')
        self.assertEqual(data_2.next_node.data, 5)




class TestStack(unittest.TestCase):
    def test_init(self):
        stack = Stack()
        self.assertEqual(stack.my_stack, [])

    def test_push(self):
        stack = Stack()
        stack.push(5)
        self.assertEqual(stack.my_stack[-1].data, 5)
        self.assertEqual(stack.my_stack[-1].next_node, None)
        stack.push("a")
        self.assertEqual(len(stack.my_stack), 2)
        self.assertEqual(stack.my_stack[-1].data, "a")
        self.assertEqual(stack.my_stack[-1].next_node, stack.my_stack[0])

