#!/usr/bin/python3
"""
 A script that takes in the name of a state as an argument
 and lists all cities of that state, using the database
 """

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities JOIN states \
                ON cities.state_id = states.id ORDER BY cities.id")
    [print(", ".join([c[2] for c in cur.fetchall() if c[4] == sys.argv[4]]))]
