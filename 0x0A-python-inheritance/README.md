# Python - Inheritance

![Drag Racing](https://forum.unity.com/attachments/u_jelly-jpg.26911/)

----
## Python Inheritance
see [Obj](https://www.w3schools.com/python/python_inheritance.asp)

> Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.

----
## usage
Create a Parent Class

Any class can be a parent class, so the syntax is the same as creating any other class:
Create a class named Person, with firstname and lastname properties, and a printname method:

    class Person:
        def __init__(self, fname, lname):
            self.firstname = fname
            self.lastname = lname

        def printname(self):
            print(self.firstname, self.lastname)


    x = Person("John", "Doe")
    x.printname()

----
## How to get started?
# Create a Child Class

    class Student(Person):
      pass

Use the Student class to create an object, and then execute the printname method:

    x = Student("Mike", "Olsen")
    x.printname()
    


----