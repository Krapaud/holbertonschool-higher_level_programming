#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
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

    # Query first State object
    state = session.query(State).order_by(State.id).first()

    # Display result or "Nothing" if empty
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    # Close session
    session.close()
