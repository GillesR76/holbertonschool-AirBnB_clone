#!/usr/bin/python3


"""
Class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User that inherits from BaseModel
    Public class Attributes:
        email(string): email of the user
        password(string): password of the user
        first_name(string): firstname of the user
        last_name(string): lastname of the user
        """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
