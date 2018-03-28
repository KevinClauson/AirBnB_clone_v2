#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from models.base_model import BaseModel
from models.base_model import Base
from os import environ
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity)

    else:
        name = ""
