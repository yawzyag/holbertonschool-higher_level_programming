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

    row = session.query(State).filter(
          State.id == '2').first()

    row.id = 2
    row.name = "New Mexico"
    session.commit()

    session.close()
