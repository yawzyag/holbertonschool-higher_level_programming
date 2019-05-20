# Python - Exceptions

![python](https://files.realpython.com/media/try_except_else.703aaeeb63d3.png "PYTHON")

----
## what is  Exceptions?
see [Exceptions](https://www.pythonforbeginners.com/error-handling/exception-handling-in-python)

> An exception is an error that happens during execution of a program. When that
error occurs, Python generate an exception that can be handled, which avoids your
program to crash.

----
## usage
The else clause in a try , except statement must follow all except clauses, and is
useful for code that must be executed if the try clause does not raise an
exception.

    try:
    data = something_that_can_go_wrong

    except IOError:
        handle_the_exception_error

    else:
        doing_different_exception_handling

----