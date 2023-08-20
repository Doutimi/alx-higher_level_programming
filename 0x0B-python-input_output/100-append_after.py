#!/usr/bin/python3
"""a function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file"""

    txt = ""
    with open(filename) as f:
        for line in f:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as q:
        q.write(txt)
