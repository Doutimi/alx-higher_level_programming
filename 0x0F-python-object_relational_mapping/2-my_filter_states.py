#!/usr/bin/python3
"""
 a script that takes in an argument and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
     Connect to the MySQL database using the provided credentials
    """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}'"
                .format(sys.argv[4]))
    [print(state) for state in cur.fetchall()]
