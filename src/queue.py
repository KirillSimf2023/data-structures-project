class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        # next_node = self.top
        # new_top = Node(data, next_node)
        # self.top = new_top
        if self.head == None:
            new_node = Node(data, None)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data, None)
            self.tail.next_node = new_node
            self.tail = new_node




    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""

        if self.head == self.tail:
            return ''

        result = []

        if self.head.next_node == None:
            return self.head.data

        next_node = self.head

        while True:
            result.append(next_node.data)
            next_node = next_node.next_node
            if next_node.next_node == None:
                result.append(next_node.data)
                break

        result_str = '\n'.join(result)

        return result_str



