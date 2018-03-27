#!/usr/bin/python3
'''
    Define the class City.
'''
from os import environ
from models.base_model import BaseModel


class City(BaseModel):
    '''
        Define the class City that inherits from BaseModel.
    '''
    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'))
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""
