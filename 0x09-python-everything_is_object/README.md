# Python - Everything is object

![Drag Racing](https://cdn-images-1.medium.com/max/800/1*7ne9uMiTvW6X0ay_rhizqw.jpeg)

----
## Everything is object
see [Obj](https://medium.com/@larmalade/python-everything-is-an-object-and-some-objects-are-mutable-4f55eb2b468b)

> Python deservedly has a reputation for being an easy language to read and write. It’s got great documentation and a community that is very welcoming to beginners. But, as you dig deeper, you may find aspects of the Python language that surprise you. One aspect that deserves in-depth explanation is variable assignment.

----
## usage

    <name> = <object>

We are actually binding a name to an object. One implication of this is that multiple names can be bound to a single object. Here is a concrete example (feel free to try this at the Python command line):

    >>> b = "spam"
    >>> print(id(a))
    140090288720896
    >>> print(id(b))
    140090288720896
    >>> print(a is b)
    True


----
## How to get started?
# What does the id() function do? 

id() returns the actual memory location where the variable is stored. Since id(a) = id(b), we know that a and b both point to a single variable, that resides in a single memory location. This is what we mean by “multiple names bound to single object”.

This broadly means, that functions in Python:

have types
can be sent as arguments to another function
can be used in expression
can become part of various data structures like dictionaries


----
