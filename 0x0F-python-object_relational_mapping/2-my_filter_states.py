#!/usr/bin/python3
""" adding comentario """


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    serv = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    c = serv.cursor()
    text = "SELECT * FROM states WHERE name LIKE '{}'\
    COLLATE latin1_general_cs\
    ORDER BY id ASC ".format(argv[4])
    c.execute(text)
    response = c.fetchall()
    for row in response:
        print(row)
    c.close()
    serv.close()
