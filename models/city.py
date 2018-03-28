#!/usr/bin/python3
'''
    Define the class City.
'''
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'))
        name = Column(String(128), nullable=False)
        places = Column(relationship("Place", backref="cities", cascade="all, delete")
    else:
        state_id = ""
        name = ""
