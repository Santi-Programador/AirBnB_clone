#!/usr/bin/python3
"""
Module for Review Class
Defines all instance attributes for a Review instance
for AirBnB Clone Project - The Console
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines attributes for all Review instances

       Public class attributes:
       place_id <string>: Place.id = <Class Place> + instance's id
       user_id <string>: User.id = <Class User> + instance's id
       text <string>: User's Review
    """
    place_id = ""
    user_id = ""
    text = ""
