#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

import os

__all__ = ['User', 'Review', 'Place', 'Amenity', 'City', 'State', 'storage']

if os.getenv("HBNB_TYPE_STORAGE") == 'db':  # db storage
    from models.engine.db_storage import DBStorage

    storage = DBStorage()
    storage.reload()
else:  # file storage
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()
