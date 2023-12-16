#!/usr/bin/python3
"""script contains a class that maps to the cities database
"""
from model_state import Base
from sqlalchemy import Integer, String, Column, ForeignKey


class City(Base):
    """class that maps to the cities database from the local machine
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
