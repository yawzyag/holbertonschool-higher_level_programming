# Python - More Data Structures: Set, Dictionary

----
## what are More Data Structures: Set, Dictionary?
see [Data Structures](https://www.oreilly.com/library/view/high-performance-python/9781449361747/ch04.html)

> Sets and dictionaries are ideal data structures to be used when your data has no intrinsic order, but does have a unique object that can be used to reference it (the reference object is normally a string, but can be any hashable type). This reference object is called the “key,” while the data is the “value.” Dictionaries and sets are almost identical, except that sets do not actually contain values: a set is simply a collection of unique keys. As the name implies, sets are very useful for doing set operations.


> Lists, strings and tuples are ordered sequences of objects. Unlike strings that contain only characters, list and tuples can contain any type of objects. Lists and tuples are like arrays. Tuples like strings are immutables. Lists are mutables so they can be extended or reduced at will. Sets are mutable unordered sequence of unique elements whereas frozensets are immutable sets.

----
##  Lists are enclosed in brackets:

```
l = [1, 2, "a"]
```

Tuples are enclosed in parentheses:

```
t = (1, 2, "a")
```

Tuples are faster and consume less memory. See Tuples for more information.

Dictionaries are built with curly brackets:

```
d = {"a":1, "b":2}
```

Defining a Dictionary
Dictionaries are Python’s implementation of a data structure that is more generally known as an associative array. A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.

Set:

```
A = {1, 2, 3}  

A = set('qwerty') 

print(A)
```

----
## Python Data Structures

You can think of a data structure as a way of organizing and storing data such that we can access and modify it efficiently. Earlier, we have seen primitive data types like integers, floats, Booleans, and strings. Now, we’ll take a deeper look at the non-primitive Python data structures.


----