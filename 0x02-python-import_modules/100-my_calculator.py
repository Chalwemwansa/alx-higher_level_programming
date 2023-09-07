#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    length = len(sys.argv) - 1
    if (length != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    match operator:
        case '+':
            result = add(a, b)
            break
        case '-':
            result = sub(a, b)
            break
        case "*":
            result = mul(a, b)
            break
        case '/':
            result = div(a, b)
            break
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))