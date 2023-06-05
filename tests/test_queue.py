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

    class TestQueue(unittest.TestCase):
        def test_init(self):
            queue = Queue()
            self.assertEqual(queue.head, None)
            self.assertEqual(queue.tail, None)


        def test_enqueue(self):
            queue = Queue()
            queue.enqueue(5)
            self.assertEqual(queue.head.data, 5)
            self.assertEqual(queue.head.next_node, None)
            queue.enqueue('a')
            self.assertEqual(queue.head.next_node.data, 'a')
            self.assertEqual(queue.tail.data, 'a')

        def test_str(self):
            self.assertEqual(str(Queue()), '')
            queue = Queue()
            queue.enqueue('data1')
            self.assertEqual(str(queue), 'data1')
            queue.enqueue('data2')
            self.assertEqual(str(queue), 'data1\ndata2')
            queue.enqueue('data3')
            self.assertEqual(str(queue), 'data1\ndata2\ndata3')

        def test_dequeue(self):
            # Создаем пустую очередь
            queue = Queue()
            # Добавляем данных в очередь
            queue.enqueue('data1')
            queue.enqueue('data2')
            queue.enqueue('data3')

            self.assertEqual(queue.dequeue(), 'data1')
            self.assertEqual(queue.dequeue(), 'data2')
            self.assertEqual(queue.dequeue(), 'data3')
            self.assertEqual(queue.dequeue(), None)
            queue.enqueue('data4')
            self.assertEqual(queue.dequeue(), 'data4')
            self.assertEqual(queue.dequeue(), None)





