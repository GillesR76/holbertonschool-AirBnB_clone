#!/usr/bin/python3


"""
Class Amenity that inherits from BaseModel
"""
from models.base_model import BaseModel
from models import storage


class Amenity(BaseModel):
    """Class Amenity that inherits from BaseModel
    Public class Attribute:
        name(string)
        """
    name = ""

    def init(self, *args, **kwargs):
        super().__init__(**kwargs)
        if kwargs:
            for key, value in kwargs.items():
                if key in ['name']:
                    if key != "__class":
                        setattr(self, key, value)
        else:
            storage.new(self)

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
