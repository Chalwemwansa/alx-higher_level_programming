#!/usr/bin/python3
import MYSQLdb
from sys import argv

def connect(usr, paswd, database):
    con = MySQLdb.connect(host="localhost", port=3306,\
            user=usr, passwd=paswd, db=database, charset="utf-8")

    cur = con.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")
    resultSet = cur.fetchall()
    for tuple in resultSet:
        print(tuple)

if __name__ == "__main__":
    connect(argv[1], argv[2], argv[3])