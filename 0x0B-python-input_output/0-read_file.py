#!/usr/bin/python3
"""A fuction that reads a file and prints to stdout"""


def read_file(filename=""):
    """"Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="UTF-8") as file:
        print(file.read(), end="")
