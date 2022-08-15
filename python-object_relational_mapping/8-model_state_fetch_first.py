#!/usr/bin/python3
"""
Script that prints the first state obj from the
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
     engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State.id, State.name).first()
    if (res is None):
        print("Nothing")
    else:
        print("{:d}: {}".format(res[0], res[1]))
