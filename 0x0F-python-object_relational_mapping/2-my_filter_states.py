#!/usr/bin/python3
""" adding comentario """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    serv = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    c = serv.cursor()
    text_exec = "SELECT * FROM states WHERE name LIKE\
    '{}' ORDER BY id ASC ".format(argv[4])
    c.execute(text_exec)
    response = c.fetchall()
    for row in response:
        print(row)
    c.close()
    serv.close()
