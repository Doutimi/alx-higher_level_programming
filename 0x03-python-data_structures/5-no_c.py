#!/usr/bin/python3

def no_c(my_string):
    # Remove all characters c and C from a string.

    n_string = ""
    for i in my_string:

        if i == "c" or i == "C":

            continue
        n_string += i
    return n_string
