#!/usr/bin/python3
"""this python script is not a module
    it is used to establish a connection and execute commands
    from the python script itself
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """this is to ensure that the script only executes when
    the script is not imported hence to use the script one has
    to just execute it without importing in their own moodule
    """
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    result = cur.fetchall()
    for tuple in result:
        print(tuple)
    cur.close()
    con.close
