#!/usr/bin/python3
""" takes in an arguement and displays all values """


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3]
    cr = db.cursor()
    cr.execute("select * from states WHERE name= '{}' ORDER BY id ASC".formart(statename))
    states = c.fetchall()
    for state in states:
            print(state)
    cr.close()
    db.close()
