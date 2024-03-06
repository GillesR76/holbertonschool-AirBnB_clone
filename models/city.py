#!/usr/bin/python3


"""
Class City that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City that inherits from BaseModel
    Public class Attributes:
        state_id(string): state id
        name(string): name of City
        """
    state_id = ""
    name = ""
