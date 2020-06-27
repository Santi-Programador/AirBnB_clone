#!/usr/bin/python3
"""
Module for User Class
Defines all instance attributes for a User instance
for AirBnB Clone Project - The Console
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines attributes for all Review instances

       Public class attributes:
       email <string>: User's e-mail
       password <string>: User's account password
       first_name <string>: User's first name
       last_name <string>: User's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
