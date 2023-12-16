#!/usr/bin/python3
"""script that prints the first State from the database given
    module can not be imported but can import other modules
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
    result = query.order_by(asc(State.id)).limit(1)
    for row in result:
        print(f"{row.id}: {row.name}")
