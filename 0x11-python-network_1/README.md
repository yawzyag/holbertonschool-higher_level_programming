# Python - Network #1

![database-python](https://3.bp.blogspot.com/--kEvzkdI6PI/XMvIZaHfzQI/AAAAAAAANTs/vRaejrVBfHklnYrecQiAp8LtEQQJrU56ACLcBGAs/s640/web_scrapping.png)

[python-urllib-module/](https://www.geeksforgeeks.org/python-urllib-module/)

---
Urllib module is the URL handling module for python. It is used to fetch URLs (Uniform Resource Locators). It uses the  _urlopen_  function and is able to fetch URLs using a variety of different protocols.

Urllib is a package that collects several modules for working with URLs, such as:

-   urllib.request for opening and reading.
-   urllib.parse for parsing URLs
-   urllib.error for the exceptions raised
-   urllib.robotparser for parsing robot.txt files


## urllib.request


This module helps to define functions and classes to open URLs (mostly HTTP). One of the most simple ways to open such URLs is :  
_urllib.request.urlopen(url)_  
We can see this in an example:
    
    import urllib.request

    request_url = urllib.request.urlopen('(https://www.geeksforgeeks.org/)')
    
    print(request_url.read())

###  urllib.parse
 
This module helps to define functions to manipulate URLs and their components parts, to build or break them. It usually focuses on splitting a URL into small components; or joining different URL components into URL string.  
We can see this from the below code:

    from urllib.parse import * parse_url = urlparse('https://www.geeksforgeeks.org / python-langtons-ant/') 
    print(parse_url) 
    print("\n") 
    unparse_url = urlunparse(parse_url) 
    print(unparse_url)

---
