#!/usr/bin/python3
"""Lists all states with name starting with N"""
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
        "SELECT * FROM states WHERe name like 'N%' ORDER BY id ASC")
    query_rows = present.fetchall()

    for row in query_rows:
        if row[1][0] == 'N':
            print(row)

    present.close()
    connect.close()
