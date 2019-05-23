#!/usr/bin/python3
""" This is necesary ? """


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        print("val is {}",format(value))
        if self.__head is None or value <= self.__head.data:
            self.__head = Node(value, self.__head)
        else:
            holi = Node(value, self.__head)
            while holi.next_node is not None and holi.next_node.data < value:
                holi = holi.next_node
            holi.next_node = Node(value, holi.next_node)

    def __str__(self):
        listm = []
        nodes = self.__head

        while nodes is not None:
            listm.append(str(nodes.data))
            nodes = nodes.next_node
        return "\n".join(listm)
