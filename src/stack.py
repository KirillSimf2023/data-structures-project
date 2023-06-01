class Node:
    """Класс для узла стека"""


    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""


    def __init__(self):
        """Конструктор класса Stack"""
        self.my_stack = []


    def __repr__(self):
        return f'{self.__class__.__name__}'


    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        if len(self.my_stack) == 0:
            new_Node = Node(data, None)
        else:
            new_Node = Node(data, None)
            self.my_stack[-1].next_node = new_Node
        self.my_stack.append(new_Node)
        self.top = new_Node


    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if len(self.my_stack)==0:
            return None
        else:
            result_Node = self.my_stack.pop(-1)
            len_stack = len(self.my_stack)
            if len_stack == 1:
                self.my_stack[0].next_node = None
                self.top = self.my_stack[0]
            elif len_stack > 1:
                self.top = self.my_stack[-1]
                self.my_stack[-1].next_node = None
            elif len_stack == 0:
                self.top = None
            return result_Node.data


