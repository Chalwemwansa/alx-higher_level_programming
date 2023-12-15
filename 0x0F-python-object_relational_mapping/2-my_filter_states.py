#!/usr/bin/python3
"""a script that only executes when is is not imported and
    retrieves values from a database according to values passed as an argument
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """section where the connection and execution of queries takes place from
    """
    querry = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY\
             id ASC".format(argv[4])
    con = MySQLdb.connect(host="localhost", port=3306, passwd=argv[2],
                          user=argv[1], db=argv[3], charset='utf8')
    cur = con.cursor()
    cur.execute(querry)
    for row in cur.fetchall():
        print(row)
    cur.close()
    con.close()
