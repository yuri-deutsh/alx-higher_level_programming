#!/usr/bin/python3
# 0-print_list_integer.py

def print_list_integer(my_list=[]):
    """Prints all intergers of a list

    Args:
      my_list: the list argument whose items will be printed
    """

    # Iterate through list
    for integer in my_list:
        print("{:d}".format(integer))
