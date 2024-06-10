""" place_amenity module for creating a relationship
between Place and Amenity

"""

import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import Table
from models.base_model import Base

if os.getenv('HBNB_TYPE_STORAGE') in ["db", "DBStorage"]:
    place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey('places.id'),
            primary_key=True,
            nullable=False
        ),
        Column(
            'amenity_id',
            String(60),
            ForeignKey('amenities.id'),
            primary_key=True,
            nullable=False
        )
    )

else:
    place_amenity = None
