#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from models.place_amenity import place_amenity


class Place(BaseModel, Base):
    """ A place to stay """

    if os.getenv('HBNB_TYPE_STORAGE') in ["db", "DBStorage"]:
        __tablename__ = "places"

        city_id = Column(
                String(60),
                ForeignKey("cities.id")
        )
        user_id = Column(
                String(60), ForeignKey("users.id"), nullable=False
        )
        name = Column(String(60), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        users = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship(
                "Review", back_populates="places", cascade="all, delete"
        )
        amenities = relationship(
                "Amenity",
                secondary=place_amenity,
                viewonly=False,
                backref="place_amenities"
        )
        amenity_ids = []

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

    def __init__(self, *args, **kwargs):
        "Initializes place"
        super().__init__(*args, **kwargs)

    if os.getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def reviews(self):
            # reviews = Storage.all(Review)
            return []
