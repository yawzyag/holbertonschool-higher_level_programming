#!/usr/bin/python3

class MyInt(int):
    def __init__(self, num):
        self.num = num
        int.__init__(self)

    def __eq__(self, juanito):
        return self.num != juanito

    def __ne__(self, juanito):
        return not self == juanito
