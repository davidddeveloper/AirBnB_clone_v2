#!/usr/bin/python3
""" Review module for the HBNB project """
import os
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """ Review classto store review information """

    if os.getenv('HBNB_TYPE_STORAGE') in ["db", "DBStorage"]:
        __tablename__ = 'reviews'

        text = Column(String(1024), nullable=False)
        place_id = Column(
                String(60), ForeignKey("places.id"), nullable=False
        )
        user_id = Column(
                String(60), ForeignKey("users.id"), nullable=False
        )
        users = relationship("User", back_populates="reviews")

    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """ Initializes Review """
        super().__init__(*args, **kwargs)
