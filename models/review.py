#!/usr/bin/python3


"""
Class Review that inherits from BaseModel
"""
from models.base_model import BaseModel
from models import storage


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

    def init(self, *args, **kwargs):
        if kwargs:
            super().init()
            for key, value in kwargs.items():
                if key in ['place_id', 'user_id', 'text']:
                    if key != "__class":
                        setattr(self, key, value)
        else:
            storage.new(self)

    def id(self):
        return super().id

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        dict_copy = super().to_dict().copy()
        try:
            dict_copy.pop('class')
        except Exception:
            pass
        dict_copy['_class'] = self.__class.__name
        for attr in ['place_id', 'user_id', 'text']:
            if hasattr(self, attr) and isinstance(getattr(self, attr), str):
                dict_copy[attr] = getattr(self, attr)
        return dict_copy
