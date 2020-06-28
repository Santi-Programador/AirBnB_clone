#!/usr/bin/python3
"""
Module for Place Class for AirBnB Clone Project - The Console
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Defines all instance attributes for a Place instance

       Public class attributes:
       city_id <string>: City.id = <Class City> + instance's id
       user_id <string>: User.id = <Class User> + instance's id
       name <string>: Name of the place
       description <string>: Description about the place
       number_rooms <int>: Number of rooms in the place
       number_bathrooms <int>:  Number of bathrooms in the place
       max_guest <int>: Max number of guest for the place
       price_by_night <int>: Price per night for the place
       latitude <float>: Latitude coordinate
       longitude <float>: Longitude coordinate
       amenity_ids <list of string>: List of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
