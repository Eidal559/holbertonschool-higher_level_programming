#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Extracting command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Creating engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Creating session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying for the State object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # If State object with id = 2 exists, update its name to "New Mexico" and commit changes
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
    else:
        print("State with id = 2 not found")
