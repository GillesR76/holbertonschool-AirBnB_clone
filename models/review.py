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

    def __init__(self, *args, **kwargs):
        """init instance method to initialize public instance
        attributes
        Attributes:
            id: string
            created_at: current datetime when an instance is created
            updated_at: updates datetime when you change the object
            """
        super().__init__(*args, **kwargs)
        if kwargs:
            for key, value in kwargs.items():
                if key in ['text', 'user_id', 'text']:
                    if key != "__class__":
                        setattr(self, key, value)
        else:
            storage.new(self)

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
