#!/usr/bin/python3


"""
Class Review that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review that inherits from BaseModel
    Public class Attributes:
        place_id(string): id of the place
        user_id(string): id of the user
        text(string)
        """
    place_id = ""
    user_id = ""
    text = ""
