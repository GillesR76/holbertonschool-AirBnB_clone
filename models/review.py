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

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        dict_copy = super().to_dict().copy()
        try:
            dict_copy.pop('__class__')
        except Exception:
            pass
        dict_copy['__class__'] = self.__class__.__name__
        for attr in ['text', 'user_id', 'text']:
            if hasattr(self, attr) and isinstance(getattr(self, attr), str):
                dict_copy[attr] = getattr(self, attr)
        return dict_copy
