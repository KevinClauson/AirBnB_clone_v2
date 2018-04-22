#!/usr/bin/python3
"""
   Creates Database Storage
"""
import models
from models.base_model import Base
from sqlalchemy import create_engine
from os import environ
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    '''
        Stores objects to a database
    '''

    __engine = None
    __session = None

    def __init__(self):
        """
            instantiates class
        """
        uname = environ.get("HBNB_MYSQL_USER")
        pwd = environ["HBNB_MYSQL_PWD"]
        host = environ["HBNB_MYSQL_HOST"]
        db = environ["HBNB_MYSQL_DB"]

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(uname, pwd, host, db),
                                      pool_pre_ping=True)

        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
           Returns all objects or specified objects
        """

        all_objs = {}
        if not cls:
            for ckey, cvalue in models.classes.items():
                query = self.__session.query(cvalue)
                for obj in query:
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    all_objs[key] = obj
        else:
            if type(cls) == str:
                cls = models.classes[cls]

            query = self.__session.query(cls)
            for obj in query:
                key = str(obj.__class__.__name__) + "." + str(obj.id)
                all_objs[key] = obj

        return all_objs

    def new(self, obj):
        """
           adds obj to db
        """
        if obj:
            self.__session.add(obj)
            self.save()

    def save(self):
        """
           commits changes to session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
           deletes obj from session
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """
           pulls stored objects from database
        """

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
           call remove() method on the private session attribute 
        """
        self.__session.remove()
