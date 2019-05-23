# Python - Test-driven development

----
## what is Test-driven development?
see [Test](https://docs.python.org/3.4/library/doctest.html#module-doctest)

> writing tests that would check the functionality of your code prior to your writing the actual code. Only when you are happy with your tests and the features it tests, do you begin to write the actual code in order to satisfy the conditions imposed by the test that would allow them to pass.

----
## usage

Following this process ensures that you careful plan the code you write in order to pass these tests. This also prevents the possibility of writing tests being postponed to a later date, as they might not be deemed as necessary compared to additional features that could be created during that time.



----
## How to get started?
# The doctest module 
Searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. There are several common ways to use doctest:

To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.
To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.

    doctest_simple.py
    def my_function(a, b):
        """
        >>> my_function(2, 3)
        6
        >>> my_function('a', 3)
        'aaa'
        """
        return a * b

----
