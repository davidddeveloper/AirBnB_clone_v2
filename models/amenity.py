#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place
from models.place_amenity import place_amenity


class Amenity(BaseModel, Base):
    """ represents amenity """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    # place_amenities = relationship(Place, back_populates="amenities")
