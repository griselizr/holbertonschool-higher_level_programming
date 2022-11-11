#!/usr/bin/python3
"""akes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
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
    present.execute("SELECT cities.name FROM cities\
        JOIN states ON cities.state_id = states.id\
            WHERE states.name=%s", (sys.argv[4], ))
    query_rows = present.fetchall()
    list = []
    for row in query_rows:
        list.append(row[0])
    print(', '.join(city[0] for city in query_rows))

    present.close()
    connect.close()
