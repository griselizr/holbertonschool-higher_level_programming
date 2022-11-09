#!/usr/bin/python3
''' lists all states from the database hbtn_0e_0_usa:

    Your script should take 3 arguments: mysql username, mysql password and database name'''

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
    present.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = present.fetchall()

    for row in query_rows:
        print(row)

    present.close()
    connect.close()
