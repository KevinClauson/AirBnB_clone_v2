#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel and Base.
    '''

    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
