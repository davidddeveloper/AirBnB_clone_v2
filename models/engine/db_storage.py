"""
    This module represents a database storage engine
    classes it defined:
        DBStorage: a database storage engine
"""
from . import setenv_env
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base, BaseModel
from models.place_amenity import place_amenity
from sqlalchemy.orm import scoped_session
from urllib.parse import quote_plus


class DBStorage:
    """
        represents a database storage engine

        Attributes:
            __engine: sqlalchemy engine
            __session: represents a session
    """
    __engine = None
    __session = None
    __mappings = {
               'users': User, 'places': Place,
               'states': State, 'cities': City, 'amenities': Amenity,
               'reviews': Review, 'place_amenity': place_amenity
              }

    def __init__(self):
        # mysql://HBNB_MYSQL_USER:HBNB_MYSQL_PWD@HBNB_MYSQL_HOST/HBNB_MYSQL_DB
        password = quote_plus(os.getenv('HBNB_MYSQL_PWD'))
        url = f"mysql://{os.getenv('HBNB_MYSQL_USER')}:{password}"
        url += f"@{os.getenv('HBNB_MYSQL_HOST')}/{os.getenv('HBNB_MYSQL_DB')}"
        self.__engine = create_engine(
            url,
            pool_pre_ping=True,
            echo=True
        )

    def all(self, cls=None):
        """
            query on the current database session

            Args:
                - cls: the class name to query for
                    otherwise query all types of objects

        """

        # Reflect metadata
        metadata = MetaData()
        metadata.reflect(bind=self.__engine)

        objects = {}
        if cls is None:
            # query all instances for all class
            for table_name in metadata.tables:
                cls = DBStorage.__mappings[table_name]
                query = self.__session.query(cls)
                result = query.all()

                for obj in result:
                    objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

            return objects  # {<class-name>.<object-id>: <obj>}

        # query all instance for a specific class
        for obj in self.__session.query(cls).all():
            objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

        return objects  # {<class-name>.<object-id>: <obj>}

    def new(self, obj):
        """
            add the object to the current database session

            Args:
                - obj: the instance to add

        """

        self.__session.add(obj)

    def save(self):
        """
            commit all changes of the current database session

        """

        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None

        Args:
            - obj: the obj to add

        """

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False)
        self.__session = scoped_session(session_factory)
        self.__session = self.__session()

        # Load the data from the database
        self.all()
