#!/usr/bin/python3
"""
    A FileStorage module
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class FileStorage:
    """
        This class serializes instances to a JSON file and deserializes JSON
        file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """A method that returns the dictionary __objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """
            A method that sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
            A method that serializes __objects to the JSON file
            (path: __file_path)
        """
#        my_dict = {}
#       for key in FileStorage.__objects.keys():
#           my_dict[key] = FileStorage.__objects[key].to_dict()
        obj_dict = FileStorage.__objects
        my_dict = {key: obj_dict[key].to_dict() for key in obj_dict.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """
            A method that deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists ; otherwise, do nothing
        """
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for value in obj_dict.values():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(cls_name)(**value))
        except FileNotFoundError:
            return
