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
    con = MySQLdb.connect(host="localhost", port=3306, passwd=argv[2],
                          user=argv[1], db=argv[3], charset="utf8")
    cur = con.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities, states
                   WHERE state_id = states.id
                   ORDER BY id""")
    for row in cur.fetchall():
        print(row)
    cur.close()
    con.close()
