#!/usr/bin/python3
"""
Module for BaseModel Class
Defines all common attributes/methods for other classes
for AirBnB Clone Project - The Console
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines the Base model and class attributes for all derived classes

       Public instance attributes:
    id <string>: Random/unique ID assigned when an instance is created
    created_at <datetime object>: current datetime when an instance is created
    updated_at <datetime object>: current datetime when an instance is updated
    """

    def __init__(self, *args, **kwargs):
        """Constructor - Sets attributes to all future instances from:
        Args:
            *args: Tuple that contains all attributes
            **kwargs: dictionary that contains all attributes by key/value args
                (Note __class__ from kwargs is not added as an attribute and
                created_at and updated_at are converted into datetime object)
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns the string representation of an instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """Updates the instance with the current datetime
        and saves it into JSON file"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary with keyworded attributes of the instance:
            * Key __class__ is added to this dictionary
              with the class name of the object
            * 'created_at' and 'updated_at' are converted to string
              objects in ISO format
        """
        inst_dict = self.__dict__.copy()
        inst_dict['__class__'] = self.__class__.__name__
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()
        return inst_dict
