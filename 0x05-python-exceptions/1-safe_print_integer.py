#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Value is not an integer")
        return False

if __name__ == "__main__":
    value = 10
    safe_print_integer(value)

    value = "hello"
    safe_print_integer(value)
