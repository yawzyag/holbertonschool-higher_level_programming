#!/usr/bin/python3
""" adding comentario """


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    serv = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = serv.cursor()
    text = "SELECT * FROM states WHERE name LIKE\
    '{}' ORDER BY id ASC ".format(argv[4])
    c.execute(text)
    response = c.fetchall()
    for row in response:
        print(row)
    c.close()
    serv.close()
