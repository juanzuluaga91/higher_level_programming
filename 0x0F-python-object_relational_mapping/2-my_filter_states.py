#!/usr/bin/python3
"""Write a script that lists all states"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    state_name = argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{:s}'ORDER BY \
        id ASC".format(state_name))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
