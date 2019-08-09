#!/usr/bin/python3
from sys import argv
import MySQLdb

serv = MySQLdb.connect(
    host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
c = serv.cursor()
c.execute("SELECT * FROM states ORDER BY id ASC")
response = c.fetchall()
for row in response:
    print(row)
