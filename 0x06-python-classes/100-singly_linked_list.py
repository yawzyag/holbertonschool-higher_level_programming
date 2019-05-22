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
        if isinstance(value, Node) or not value:
            raise TypeError("data must be an integer")
        else:
            self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        pass

    def sorted_insert(self, value):
        pass
