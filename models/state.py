#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    id = Column(String, primary_key=True,
                                nullable=False,
                                unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship(City, back_populates="state", cascade="all, delete")
