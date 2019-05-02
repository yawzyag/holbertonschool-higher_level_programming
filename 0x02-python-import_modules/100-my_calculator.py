#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        symbol = sys.argv[2]

        if symbol == "+":
            print("{:d} + {:d} = {:d}".format(a, b, a + b))
        elif symbol == "-":
            print("{:d} - {:d} = {:d}".format(a, b, a - b))
        elif symbol == "*":
            print("{:d} * {:d} = {:d}".format(a, b, a * b))
        elif symbol == "/":
            print("{:d} / {:d} = {:f}".format(a, b, a / b))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
