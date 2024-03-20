#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = createengine('mysql+mysqldb://{}:{}@{}/{}'
                .format(user, passwd, host, db), pool_pre_ping=True)

        if env == "test":
            Base.metdata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retun a dictionary"""
        d_ctionary = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
                querry = self.__session.querry(cls)
                for element in querry:
                    key = "{}.{}".format(type(element).__name__, element.id)
                    d_ctionary[key] = element
                else:
                    l_ist = [State, city, User, Place, Review, Amenity]
                    for case in l_ist:
                        querry = self.__session.query(case)
                        for element in querry:
                            key = "{}.{}".format(type(element).__name__, element.id)
                            d_ctionary[key] = element
                return (d_ctionary)

    def new(self, obj):
        """add a new element in the table
        """
        self.__session.add(obj)

    def save(self):
        """save changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """Configuration"""
        Base.metadata.create_all(self.__engine)
        s = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(s)
        self.__session = session()

    def close(self):
        """Call remove"""
        self.__session.close()

