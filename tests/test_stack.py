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
        self.assertEqual(stack.top.data, 5)
        self.assertEqual(stack.top.next_node, None)
        stack.push("a")
        self.assertEqual(stack.top.data, "a")


    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        data = stack.pop()
        #Проверяем удаленный элемент
        self.assertEqual(data, 'data1')
        # Проверяем что stack пустой, то есть в его вершине ничего нет
        self.assertEqual(stack.top, None)
        # Проверяем что stack пустой, при команде pop вернет None
        self.assertEqual(stack.pop(), None)

        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        data = stack.pop()
        self.assertEqual(data, 'data3')
        data = stack.pop()
        self.assertEqual(data, 'data2')

        # Проверяем что остался всего 1 элемент с данными data1
        self.assertEqual(stack.top.data, 'data1')






