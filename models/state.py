#!/usr/bin/python3
'''
    Implementation of the State class
'''
import models
from os import environ
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """
               getter for file storage
            """
            city_objs = {}
            city_objs = models.storage.all(City)
            match_cities = []
            for key, value in city_objs.items():
                if value.state_id == self.id:
                    match_cities.append(value)
            return match_cities
