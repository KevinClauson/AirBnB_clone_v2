#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    '''
        Definition of the User class
    '''
    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place",
                              backref="user",
                              cascade="all, delete")
        reviews = relationship("Review",
                               backref="user",
                               cascade="all, delete")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
