#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # database storage
    if os.environ["HBNB_TYPE_STORAGE"] == "db":
        cities = relationship("City", backref="state", cascade="delete")
    # file storage
    else:
        @property
        def cities(self):
            """
               getter for file storage
            """
            city_objs = {}
            city_objs = models.storage.all(City)
            match_cities = []
            for key, value in city_objs:
                print("KEY: ", key)
                print("Value: ", value)
                if value.state_id == self.id:
                    match_cities.append(value)
            return match_cities
