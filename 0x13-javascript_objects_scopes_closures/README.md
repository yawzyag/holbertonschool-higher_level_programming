# Classes in JavaScript

![class](https://www.unionsquaredesign.com/wp-content/uploads/2016/10/CPT-OOP-objects_and_classes_-_attmeth.svg-300x239.png)

[classes](https://www.digitalocean.com/community/tutorials/understanding-classes-in-javascript)

---

JavaScript is a prototype-based language, and every object in JavaScript has a hidden internal property called [[Prototype]] that can be used to extend object properties and methods. You can read more about prototypes in our Understanding Prototypes and Inheritance in JavaScript tutorial. Until recently, industrious developers used constructor functions to mimic an object-oriented design pattern in JavaScript. The language specification ECMAScript 2015, often referred to as ES6, introduced classes to the JavaScript language. Classes in JavaScript do not actually offer additional functionality, and are often described as providing “syntactical sugar” over prototypes and inheritance in that they offer a cleaner and more elegant syntax. Because other programming languages use classes, the class syntax in JavaScript makes it more straightforward for developers to move between languages.

## Classes Are Functions


A JavaScript class is a type of function. Classes are declared with the  `class`  keyword. We will use function expression syntax to initialize a function and class expression syntax to initialize a class.

```js
// Initializing a function with a function expression
const x = function() {}

```

```js
// Initializing a class with a class expression
const y = class {}

```

We can access the  `[[Prototype]]`  of an object using the  [`Object.getPrototypeOf()`  method](https://www.digitalocean.com/community/tutorials/understanding-prototypes-and-inheritance-in-javascript#javascript-prototypes). Let’s use that to test the empty  **function**  we created.

```js
Object.getPrototypeOf(x);

```

```

```

We can also use that method on the  **class**  we just created.

```js
Object.getPrototypeOf(y);

```

```

```

The code declared with  `function`  and  `class`  both return a function  `[[Prototype]]`. With prototypes, any function can become a constructor instance using the  `new`  keyword.

```js
const x = function() {}

// Initialize a constructor from a function
const constructorFromFunction = new x();

console.log(constructorFromFunction);

```
```

This applies to classes as well.

```js
const y = class {}

// Initialize a constructor from a class
const constructorFromClass = new y();

console.log(constructorFromClass);

```

```

```

These prototype constructor examples are otherwise empty, but we can see how underneath the syntax, both methods are achieving the same end result.

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