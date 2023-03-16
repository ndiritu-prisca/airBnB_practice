#!/usr/bin/python3
"""A module that defines all common attributes/methods for other classes"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Defining the class"""
    def __init__(self, *args, **kwargs):
        """
            Class constructor

            Args:
                *args: Unused
                **kwargs (dict): key/value pairs of attributes
        """
        format_str = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, format_str)
                else:
                    self.__dict__[key] = value
        else:
             models.storage.new(self)

    def __str__(self):
        """
            This method returns [<class name>] (<self.id>) <self.__dict__>
        """
        clname = self.__class__.__name__
        return ("[{}] ({}) {}".format(clname, self.id, self.__dict__))

    def save(self):
        """
            This method updates the public instance attribute updated_at with
            the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
            This method  returns a dictionary containing all keys/values of
            __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return (my_dict)
