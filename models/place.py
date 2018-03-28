#!/usr/bin/python3
'''
    Define the class Place.
'''
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


if environ.get('HBNB_TYPE_STORAGE') == 'db':
        metadata = Base.metadata
        place_amenity = Table("place_amenity", metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'), primary_key=True,
                                     nullable=False),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     primary_key=True,
                                     nullable=False))


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """
               getter for file storage
            """
            review_objs = {}
            review_objs = models.storage.all(Review)
            match_reviews = []
            for key, value in review_objs:
                if value.place_id == self.id:
                    match_reviews.append(value)
            return match_reviews

        @property
        def amenities(self):
            """
               getter for file storage
            """
            amenity_objs = {}
            amenity_objs = models.storage.all(Amenity)
            match_amenities = []
            for key, value in amenity_objs:
                if value.amenity_id == self.id:
                    match_amenities.append(value)
            return match_amenities

        @amenities.setter
        def amenities(self, obj):
            """
               setter for file storage
            """

            if type(obj) == models.classes["Amenity"]:
                amenity_ids.append(obj.id)
