#!/usr/bin/python3


"""
Class Place that inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class Place that inherits from BaseModel
    Public class Attributes:
        city_id(string): id of the city
        user_id(string): id of the user
        name(string)
        description(string)
        number_rooms(int): number of rooms
        number_bathrooms(int): number of bathrooms
        max_guest(int): max number of guests
        price_by_night(int): price per night
        latitude(float)
        longitude(float)
        amenity_ids(list): list of string
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

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        dict_copy = super().to_dict().copy()
        try:
            dict_copy.pop('class')
        except Exception:
            pass
        dict_copy['__class__'] = self.__class__.__name__
        for attr in ['city_id', 'user_id', 'name', 'description', 'number_rooms',
                           'number_bathrooms', 'max_guest', 'price_by_night',
                           'latitude', 'longitude', 'amenity_ids']:
            if hasattr(self, attr):
                dict_copy[attr] = getattr(self, attr)
        return dict_copy
