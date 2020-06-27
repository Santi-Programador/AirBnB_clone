#!/usr/bin/python3
"""
Module for Amenity Class
Defines all instance attributes for an Amenity instance
for AirBnB Clone Project - The Console
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines attributes for all Amenity instances

       Public class attributes:
       name <string>: Name of the amenity
    """
    name = ""
