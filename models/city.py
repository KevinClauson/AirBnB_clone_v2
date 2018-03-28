#!/usr/bin/python3
'''
    Define the class City.
'''
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    '''Define the class City that inherits from BaseModel.'''

    if (environ.get('HBNB_TYPE_STORAGE') == 'db'):
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", cascade='all, delete-orphan',
                              backref='cities')
    else:
        state_id = ''
        name = ''
