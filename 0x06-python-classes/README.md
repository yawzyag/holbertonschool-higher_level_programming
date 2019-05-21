# Python - Object Oriented

----
## what is Object Oriented?
see [Object Oriented](https://www.tutorialspoint.com/python/python_classes_objects.htm)

> Python has been an object-oriented language since it existed. Because of this, creating and using classes and objects are downright easy. This chapter helps you become an expert in using Python's object-oriented programming support.

----
## Overview of OOP Terminology

### Class 
A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.

### Class variable 
A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. Class variables are not used as frequently as instance variables are.

### Data member 
 A class variable or instance variable that holds data associated with a class and its objects.

### Function overloading 
The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.

###Instance variable 
A variable that is defined inside a method and belongs only to the current instance of a class.

###Inheritance 
The transfer of the characteristics of a class to other classes that are derived from it.

###Instance
An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.

###Instantiation 
The creation of an instance of a class.

###Method 
A special kind of function that is defined in a class definition.

###Object
 A unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance variables) and methods.

###Operator overloading 
The assignment of more than one function to a particular operator.

----
## Creating Classes
The class statement creates a new class definition. The name of the class immediately follows the keyword class followed by a colon as follows

    class ClassName:
        'Optional class documentation string'
         class_suite

The class has a documentation string, which can be accessed via ClassName.___doc___.

The class_suite consists of all the component statements defining class members, data attributes and functions.

----
## Example

    class Employee:
        'Common base class for all employees'
        empCount = 0

       def __init__(self, name, salary):
          self.name = name
          self.salary = salary
          Employee.empCount += 1
   
      def displayCount(self):
          print "Total Employee %d" % Employee.empCount

      def displayEmployee(self):
          print "Name : ", self.name,  ", Salary: ", self.salary

The variable __empCount__ is a class variable whose value is shared among all instances of a this class. This can be accessed as Employee.empCount from inside the class or outside the class.

The first method ___init___() is a special method, which is called class constructor or initialization method that Python calls when you create a new instance of this class.

You declare other class methods like normal functions with the exception that the first argument to each method is self. Python adds the self argument to the list for you; you do not need to include it when you call the methods.

----