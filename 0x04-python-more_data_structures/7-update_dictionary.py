#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to replace or add key/value in a dictionary
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for i in a_dictionary:
            if i == key:
                a_dictionary[i] = value
    return a_dictionary
