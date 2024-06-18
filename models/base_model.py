#!/usr/bin/python3
"""This module defines base model for Easy Freight
   This module provides the BaseModel class used as
   a foundation for other entity classes.
"""

from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object

time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """The BaseModel class serves as a base for future class creations.
       It includes id, created_at, and updated_at attributes with automatic
       handling.
    """

     if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        Attributes can be set via kwargs with automatic id and
        timestamp generation.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if not getattr(self, "id", None):
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """
           Generates a string representation of the BaseModel instance,
           showcasing its class name, id, and dictionary representation.
           Returns a string representation of the base model instance.
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime
        and saves the instance to storage.
        Raises:
            NotImplementedError: If the storage module is not implemented.
        """
        self.updated_at = datetime.utcnow()
        try:
            models.storage.new(self)
            models.storage.save()
        except ImportError:
            raise NotImplementedError("storage module not implemented")

    def to_dict(self):
        """
        Creates a dictionary representation of the instance,
        including formatted timestamps and excluding private attributes.
        Returns a dictionary representation of the base model instance.
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = new_dict["created_at"].strftime(time)
        new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        del new_dict["_sa_instance_state"]  # Remove SQLAlchemy internal state
        if "password" in new_dict:
            del new_dict["password"]  # Exclude password for security
        return new_dict

    def delete(self):
        """
        Deletes/remove the current instance from the storage.
        Raises:
            NotImplementedError: If the storage module is not implemented.
        """
        try:
            models.storage.delete(self)
        except ImportError:
            raise NotImplementedError("storage module not implemented")
