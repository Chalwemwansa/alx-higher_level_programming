#!/usr/bin/python3
"""script that prints any city containg the letter a in it
    script can not be imported
"""
from sys import argv
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/\
{argv[3]}", pool_pre_ping=True)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State)

    result = query.filter(State.name.ilike('%a%')).order_by(asc(State.id))
    for row in result:
        print(f"{row.id}: {row.name}")
