#!/usr/bin/python3
"""
Module for FileStorage Class
Data and Storage Management for the AirBnB Clone Project - The Console
"""

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Defines the File Storage and class attributes for all derived classes

       Private class attributes:
       __file_path <string>: path to the JSON file
       __objects <dictionary>: store all objects by '<class name>.id'
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the class attribute '__objects <dictionary>'"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in '__objects' the <obj> with key '<obj class name>.id'"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file '__file_path'"""
        dict_to_json = FileStorage.__objects.copy()  # should or not be a copy?
        dict_to_json = {k: v.to_dict() for k, v in dict_to_json.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as jfile:
            json.dump(dict_to_json, jfile)

    def reload(self):
        """Deserializes the JSON file to '__objects':
        Checks existence of the JSON file, reads data and instantiates every
        dictionary representation according the ['__class__'] name
        """
        file = FileStorage.__file_path
        if path.exists(file):
            with open(file, 'r', encoding='utf-8') as jfile:
                FileStorage.__objects = json.load(jfile)
                for key, value in FileStorage.__objects.items():
                    c = FileStorage.__objects[key]['__class__']
                    FileStorage.__objects[key] = self.find_class(c)(**value)

    def find_class(self, str_class):
        """Returns class according input to instantiate obj when is called
        Args:
            str_class <string>: Name of the requested Class"""
        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }
        return classes[str_class]
