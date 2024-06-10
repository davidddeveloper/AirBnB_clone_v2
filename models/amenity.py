#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place
from models.place_amenity import place_amenity


class Amenity(BaseModel, Base):
    """ represents amenity """

    if os.getenv('HBNB_TYPE_STORAGE') in ["db", "DBStorage"]:
        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)
        # place_amenities = relationship(Place, back_populates="amenities")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes Amenity """
        super().__init__(*args, **kwargs)
