#!/usr/bin/python3
""" This is necesary ? """


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node or value is not None:
            raise TypeError("data must be an integer")
        else:
            self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = self.__head
        if self.__head is None:
            self.__head = new_node
        else:
            while new_node.next_node is not None:
                new_node = new_node.next_node
            new_node.next_node = Node(value, new_node)
