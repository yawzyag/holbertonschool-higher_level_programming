#!/usr/bin/python3
""" adding comentario """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    serv = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    c = serv.cursor()
    c.execute("SELECT cities.name\
              FROM cities WHERE cities.state_id = \
              (SELECT states.id FROM states WHERE \
              states.name = %s) ORDER BY cities.id ASC;", (argv[4],))
    response = c.fetchall()
    strings = []
    for item in response:
        strings += item
    print(", ".join(strings))
    c.close()
    serv.close()
