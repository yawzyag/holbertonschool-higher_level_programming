#!/usr/bin/python3
"""Start link class to table in database"""

if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    from model_state import Base, State
    from sqlalchemy import desc, asc

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name == sys.argv[4]).all()
    # print(type(result))
    if len(result) != 0:
        for row in result:
            print("{}".format(row.id))
    else:
        print("Not found")
    session.close()
