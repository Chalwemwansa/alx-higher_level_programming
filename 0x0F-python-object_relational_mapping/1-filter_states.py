#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
    the module contains a function connect that establishes a connection to
    a mysql database
"""
import MySQLdb
from sys import argv


def connect(usr, paswd, database):
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'
    the function establishes a connection to a mysqldb from python and allows
    performing of querries using the function
    """
    con = MySQLdb.connect(host="localhost", port=3306,
                          user=usr, passwd=paswd, db=database)

    cur = con.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC", ('N%',))
    resultSet = cur.fetchall()
    for tuple in resultSet:
        print(tuple)
    cur.close()
    con.close()


if __name__ == "__main__":
    connect(argv[1], argv[2], argv[3])
