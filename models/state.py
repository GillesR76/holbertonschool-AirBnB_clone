#!/usr/bin/python3


"""
Class State that inherits from BaseModel
"""
from models.base_model import BaseModel
from models import storage


class State(BaseModel):
    """Class State that inherits from BaseModel
    Public class Attribute:
        name(string): name of the State
        """
    name = ""

    def init(self, *args, **kwargs):
        if kwargs:
            super().init()
            for key, value in kwargs.items():
                if key in ['name']:
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
        for attr in ['name']:
            if hasattr(self, attr) and isinstance(getattr(self, attr), str):
                dict_copy[attr] = getattr(self, attr)
        return dict_copy
