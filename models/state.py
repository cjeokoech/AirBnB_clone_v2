#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import models
from sqlalchemy.orm import relationship
from models.city import City
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan', backref="state")

    @property
    def cities(self):
        variable = models.storage.all()
        l_ist = []
        result = []
        for key in variable:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                l_ist.append(variable[key])
            for element in l_ist:
                if (element.state_id == self.id):
                    result.append(element)
            return (result)
