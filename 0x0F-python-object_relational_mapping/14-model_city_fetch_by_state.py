#!/usr/bin/python3
"""prints all the city objects from a given database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, asc, label
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/\
{argv[3]}", pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State.name.label('state_name'), City.id, City.name)

    rst = query.filter(City.state_id == State.id).order_by(asc(City.id)).all()
    for row in rst:
        print(f"{row.state_name}: ({row.id}) {row.name}")
