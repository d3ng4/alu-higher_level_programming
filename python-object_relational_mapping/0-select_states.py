#!/usr/bin/python3
""" List all states from the database bhtn_0c_0_usa """


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
            passwd=argv[2],
            db=argv[3]
    cr = db.current()
    cp.execute("SELECT * from states ORDER BY states.id")
    states = cr.fetchall()
    for state in states:
         print(states)
    cr.close()
    db.close()
