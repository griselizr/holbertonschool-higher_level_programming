#!/usr/bin/python3
"""that lists all cities from the database hbtn_0e_4_usa
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
    present.execute("""SELECT cities.id, cities.name,
                    states.name FROM cities, states WHERE \
                        cities.state_id = states.id ORDER BY cities.id ASC""")
    query_rows = present.fetchall()

    for row in query_rows:
        print(row)

    present.close()
    connect.close()
