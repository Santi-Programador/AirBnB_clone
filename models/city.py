#!/usr/bin/python3
"""
Module for City Class
Defines all instance attributes for a City instance
for AirBnB Clone Project - The Console
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Defines attributes for all City instances

       Public class attributes:
       state_id <string>: State.id = <Class State> + instance's id
       name <string>: City ​​name of the place
    """
    state_id = ""
    name = ""
