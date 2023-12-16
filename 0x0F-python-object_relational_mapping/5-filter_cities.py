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
    querry = """SELECT name
                FROM cities
                WHERE state_id = (
                    SELECT id
                    FROM states
                    WHERE name LIKE BINARY %s
                )
                ORDER BY id"""
    con = MySQLdb.connect(host="localhost", port=3306, passwd=argv[2],
                          user=argv[1], db=argv[3], charset="utf8")
    cur = con.cursor()
    cur.execute(querry, (argv[4],))
    result = cur.fetchall()
    prt = ", ".join(value[0] for value in result)
    print(prt)
    cur.close()
    con.close()
