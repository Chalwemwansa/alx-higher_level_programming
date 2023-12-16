#!/usr/bin/python3
"""script that queries a database to get the list of cities
    from a db in ascending order
"""
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/\
{argv[3]}", pool_pre_ping=True)

    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State)

    for state in query.order_by(asc(State.id)).all():
        print(f"{state.id}: {state.name}")
