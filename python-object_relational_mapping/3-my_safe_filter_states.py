#!/usr/bin/python3
"""write one that is safe from MySQL injections!"""
import MySQLdb
import sys

if __name__ == "__main__":

    connect = MySQLdb.connect(host="localhost",
                              port=3306,
                              user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3],
                              charset="utf8")
    present = connect.cursor()
    present.execute(
        "SELECT * FROM states WHERE BINARY name='%s' ORDER BY id ASC"[sys.argv[4]])
    query_rows = present.fetchall()

    for row in query_rows:
        print(row)

    present.close()
    connect.close()
