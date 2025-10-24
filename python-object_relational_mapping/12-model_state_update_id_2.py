#!/usr/bin/python3
"""
Script that changes the name of a State object where id = 2
to "New Mexico" in the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State object with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Update the name to "New Mexico"
    if state:
        state.name = "New Mexico"
        # Commit the session
        session.commit()

    # Close session
    session.close()
