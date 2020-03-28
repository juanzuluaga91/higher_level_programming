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
    cmd_q = "SELECT cities.name FROM cities \
             JOIN states ON states.id = cities.state_id \
             WHERE states.name =%s"
    cur.execute(cmd_q,(state_name,))
    c = int(cur.rowcount)
    for i, row in enumerate(cur.fetchall()):
        if i < c -1:
            print(row[0], end=", ")
        else:
            print (row[0])
    cur.close()
    db.close()
