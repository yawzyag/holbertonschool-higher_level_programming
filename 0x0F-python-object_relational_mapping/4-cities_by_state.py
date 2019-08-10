#!/usr/bin/python3
""" adding comentario """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    serv = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    c = serv.cursor()
    c.execute("SELECT cities.id, cities.name, states.name\
              FROM cities JOIN states ON cities.state_id=states.id\
              ORDER BY cities.id ASC")
    response = c.fetchall()
    for row in response:
        print("{}".format(row))
    c.close()
    serv.close()
