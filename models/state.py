#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """

    if os.getenv('HBNB_TYPE_STORAGE') in ["db", "DBStorage"]:
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship(
                City,
                backref="state"
        )
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize states """
        super().__init__(*args, **kwargs)

    if os.getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """ Retrives cities associated with a specific state by """
            from models.__init__ import storage

            all_cities = storage.all(City)

            # get cities associated with specific state
            cities_in_state = []
            for city_obj in all_cities.values():
                try:
                    if city_obj.state_id == self.id:
                        # city associated with state
                        cities_in_state.append(city_obj)
                except IndexError:
                    pass

            return cities_in_state
