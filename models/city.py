#!/usr/bin/python3
""" City Module for HBNB project """
import os
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    # state = relationship("State", back_populates="cities")
    places = relationship(
            Place, back_populates="cities", cascade="all, delete"
    )

    if os.getenv('HBNB_TYPE_STORAGE') in ["db", "DBStorage"]:
        state = relationship("State", back_populates="cities")
