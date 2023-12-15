#!/usr/bin/python3
import MySQLdb
from sys import argv
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def connect(usr, paswd, database):
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """
    con = MySQLdb.connect(host="localhost", port=3306,
                          user=usr, passwd=paswd, db=database, charset="utf8")

    cur = con.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    resultSet = cur.fetchall()
    for tuple in resultSet:
        print(tuple)


if __name__ == "__main__":
    connect(argv[1], argv[2], argv[3])
