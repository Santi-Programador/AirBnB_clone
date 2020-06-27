#!/usr/bin/python3
"""
Module for FileStorage Class
Data and Storage Management for the AirBnB Clone Project - The Console
"""
import json
from os import path


class FileStorage:
    """Defines the FileStorage and class attributes for all derived classes
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
        """Deserializes the JSON file to '__objects'"""
        # IT WORKS - BUT IS UNDER REFACTOR ACCORDING DIFFERENT OBJECT CLASSES
        from models.base_model import BaseModel
        file = FileStorage.__file_path
        if path.exists(file):
            with open(file, 'r', encoding='utf-8') as jfile:
                from_json = json.load(jfile)
                # print(from_json['BaseModel.277b0c46-a9dc-453a-ba0c-808898f242ee']['__class__'])
                from_json = {k: BaseModel(**v) for k, v in from_json.items()}
                FileStorage.__objects = from_json
