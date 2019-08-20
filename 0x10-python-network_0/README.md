# Python - Network #0

![database-python](https://cdn.lynda.com/course/772337/772337-636742488804326502-16x9.jpg)

[Reference](https://www.tutorialspoint.com/python/python_networking.htm#)

---
Python provides two levels of access to network services. At a low level, you can access the basic socket support in the underlying operating system, which allows you to implement clients and servers for both connection-oriented and connectionless protocols.

Python also has libraries that provide higher-level access to specific application-level network protocols, such as FTP, HTTP, and so on.

This chapter gives you understanding on most famous concept in Networking - Socket Programming.

## What is Sockets?

Sockets are the endpoints of a bidirectional communications channel. Sockets may communicate within a process, between processes on the same machine, or between processes on different continents.

Sockets may be implemented over a number of different channel types: Unix domain sockets, TCP, UDP, and so on. The  _socket_  library provides specific classes for handling the common transports as well as a generic interface for handling the rest.

###  HTTP headers

 
HTTP headers allow the client and the server to pass additional information with the request or the response. An HTTP header consists of its case-insensitive name followed by a colon '`:`', then by its value (without line breaks). Leading white space before the value is ignored.

---