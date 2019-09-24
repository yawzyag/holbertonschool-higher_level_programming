# Javascript - Web scraping

![class](https://cdn-media-1.freecodecamp.org/images/1*gqHgCNubMncv7EwWNdArGQ.png)

[request module](https://stackabuse.com/the-node-js-request-module/)

---

These days our web applications tend to have a lot of integrations with other services, whether it be interacting with a REST service like Twitter, or downloading images from Flickr. Using Node/JavaScript is one of the most popular languages to handle applications like this. Either way, you'll be making a lot of HTTP requests, which means you'll need a solid module to make writing the code much more bearable. The request module is by far the most popular (non-standard) Node package for making HTTP requests. Actually, it is really just a wrapper around Node's built in http module, so you can achieve all of the same functionality on your own with http, but request just makes it a whole lot easier.

## Making HTTP Requests

While there are quite a few options available to you in  `request`  (many of which we'll cover throughout this article), it can be pretty simple to use as well. The "hello world" example for this library is as easy as passing a URL and a callback:

```javascript
const request = require('request');

request('http://stackabuse.com', function(err, res, body) {
    console.log(body);
});

```

The code above submits an HTTP GET request to stackabuse.com and then prints the returned HTML to the screen. This type of request works for any HTTP endpoint, whether it returns HTML, JSON, an image, or just about anything else.

The first argument to  `request`  can either be a URL string, or an object of options. Here are some of the more common options you'll encounter in your applications:

-   `url`: The destination URL of the HTTP request
-   `method`: The HTTP method to be used (GET, POST, DELETE, etc)
-   `headers`: An object of HTTP headers (key-value) to be set in the request
-   `form`: An object containing key-value form data

```javascript
const request = require('request');

const options = {
    url: 'https://www.reddit.com/r/funny.json',
    method: 'GET',
    headers: {
        'Accept': 'application/json',
        'Accept-Charset': 'utf-8',
        'User-Agent': 'my-reddit-client'
    }
};

request(options, function(err, res, body) {
    let json = JSON.parse(body);
    console.log(json);
});
```

Using the  `options`  object, this request uses the GET method to retrieve JSON data directly from Reddit, which is returned as a string in the  `body`  field. From here, you can use  `JSON.parse`  and use the data as a normal JavaScript object.

This same request format can be used for any  [type of HTTP method](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods), whether it's DELETE, PUT, POST, or OPTIONS. Although, not all methods are used exactly the same. Some, like the POST method, can include data within the request. There are a few ways this data can be sent, some of which are:

-   `body`: A  `Buffer`,  `String`, or  `Stream`  object (can be an object if  `json`  option is set to  `true`)
-   `form`: An object of key-value pair data (we'll go over this later)
-   `multipart`: An array of objects that can contain their own headers and body attributes

Each fulfills a different need (and there are even more ways to send data, which can be found in  [this section of request's README](https://www.npmjs.com/package/request#requestoptions-callback)). The  `request`  module does contain some convenience methods that make these a bit easier to work with, however, so be sure to read the full docs to avoid making your code more difficult than it has to be.

Speaking of helper methods, a much more succinct way of calling the different HTTP methods is to use the respective helper methods provided. Here are a few of the more commonly used ones:

-   `request.get(options, callback)`
-   `request.post(options, callback)`
-   `request.head(options, callback)`
-   `request.delete(options, callback)`

While this won't save you a ton of lines of code, it will at least make your code a bit easier to understand by allowing you to just look at the method being called and not having to parse through all of the various options to find it.


## Defining a Class


A  **constructor function**  is initialized with a number of parameters, which would be assigned as properties of  `this`, referring to the function itself. The first letter of the identifier would be capitalized by convention.

constructor.js

```js
// Initializing a constructor function
function Hero(name, level) {
    this.name = name;
    this.level = level;
}

```

When we translate this to the  **class**  syntax, shown below, we see that it is structured very similarly.

class.js

```js
// Initializing a class definition
class Hero {
    constructor(name, level) {
        this.name = name;
        this.level = level;
    }
}

```

We know a constructor function is meant to be an object blueprint by the capitalization of the first letter of the initializer (which is optional) and through familiarity with the syntax. The  `class`  keyword communicates in a more straightforward fashion the objective of our function.

The only difference in the syntax of the initialization is using the  `class`  keyword instead of  `function`, and assigning the properties inside a  `constructor()`  method.

---