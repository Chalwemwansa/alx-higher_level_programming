#!/usr/bin/python3
"""link class for states table, this module has to be imported to
    be used to map a relational database to python objects
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """the class that will be used to link to a relational database
    from python
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
