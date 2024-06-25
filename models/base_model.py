#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import os
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

if os.getenv('HBNB_TYPE_STORAGE') in ["db", "DBStorage"]:
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    if os.getenv('HBNB_TYPE_STORAGE') in ["db", "DBStorage"]:
        id = Column(
                String(60), primary_key=True
        )
        created_at = Column(
                DateTime,
                default=datetime.utcnow,
                nullable=False
        )
        updated_at = Column(
                DateTime,
                default=datetime.utcnow,
                nullable=False
        )

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

            if kwargs.get('updated_at', None) and type(self.updated_at) is str:
                kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'],
                        '%Y-%m-%dT%H:%M:%S.%f'
                )
            else:
                self.updated_at = datetime.utcnow()

            if kwargs.get('created_at', None) and type(self.created_at) is str:
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'],
                        '%Y-%m-%dT%H:%M:%S.%f'
                )
            else:
                self.created_at = datetime.utcnow()

            if kwargs.get('id', None) is None:
                self.id = str(uuid.uuid4())

            # self.__dict__.update(kwargs)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]

        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        try:
            del dictionary['_sa_instance_state']
        except Exception:
            pass
        return dictionary

    def delete(self):
        """deletes the current instance from the storage"""
        from models import storage

        instance = storage.all()['{}.{}'.format(self.__class__.__name__, self.id)]
        if instance is not None:
            storage.delete(instance)
