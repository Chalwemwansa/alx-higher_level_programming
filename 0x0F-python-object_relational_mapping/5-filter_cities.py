#!/usr/bin/python3
"""script that prints different cities present in a database
    can not work if imported only works when run as a script
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """the part of the script that will be excuted when script is run
    takes three arguments only
    """
    querry = """SELECT cities.name
                FROM cities, states
                WHERE state_id = states.id
                AND states.name LIKE BINARY %s
                ORDER BY cities.id"""
    con = MySQLdb.connect(host="localhost", port=3306, passwd=argv[2],
                          user=argv[1], db=argv[3], charset="utf8")
    cur = con.cursor()
    cur.execute(querry, (argv[4],))
    result = cur.fetchall()
    length = len(result)
    for row in range(length):
        print(result[row][0], end="")
        if row == length - 1:
            print()
        else:
            print(", ", end="")
    cur.close()
    con.close()
