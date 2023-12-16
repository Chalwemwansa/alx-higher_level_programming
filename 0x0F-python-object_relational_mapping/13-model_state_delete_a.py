#!/usr/bin/python3
"""the script deletes every object whose name has a in it
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/\
{argv[3]}", pool_pre_ping=True)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State)
    obj_list = query.filter(State.name.ilike('%a%')).all()

    for obj in obj_list:
        session.delete(obj)
    session.commit()
