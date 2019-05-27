# Python - More Classes and Objects

![Drag Racing](https://community-cdn-digitalocean-com.global.ssl.fastly.net/assets/tutorials/images/large/EBOOK_PYTHON_no-name.png?1516826609)

----
## what is Classes and Objects?
see [Test](https://medium.com/@DakshHub/object-oriented-python-class-es-and-object-s-f9f016674e40)

> Object Oriented Programming is most widely used programming paradigm of the day and almost all of them provides a way to create and manage Objects. Here is what is meant by an Object.

> Similar to other OOP languages, the class in python provides a blueprint to create objects. Just as we store postal addresses in dictionaries above, we can also store them using objects of the class too.

----
## usage

    class PostalAddress:
        pass

    cP1 = PostalAddress()
    # Create an Instance for person ABC
    cP1.name = "ABC"
    cP1.street = "Central Street - 1"

    # Create an Instance for person DEF
    cP2 = PostalAddress()
    cP2.name = "DEF"
    cP2.street = "Central Street - 2"



----
## How to get started?
# The __init__(…) function
Python provides special functions for objects which is prefixed and suffixed by `__`. The function __dict__ which we have used earlier was also a special function of similar type

The function __init__ is called whenever an object is created. The function takes one mandatory parameter which is called self. Here self refers to the object itself.

    class PostalAddress:
    def __init__(self):
        pass

It’s inside this __init__ function, we create local instance variables which define the state (identifiable characteristics) of the object built out of this class.

----
