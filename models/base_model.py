#!/usr/bin/python3


"""
* Write a class BaseModel that defines all common
attributes/methods for other classes

* Public instance attributes:
    id:string - assign with an uuid when an instance is created
    created_at:datetime - assign with the current datetime when an
instance is created
    updated_at:datetime - assign with the current datetime when an instance
is created and it will be updated every time you change your object

* Public instance methods:
    save(self):updates the public instance attribute updated_at with the
current datetime
    to_dict(self):returns a dictionary containing all keys/values
of __dict__ of the instance
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class BaseModel that defines all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """init instance method to initialize public instance
        attributes
        Attributes:
            id: string
            created_at: current datetime when an instance is created
            updated_at: updates datetime when you change the object
            """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
            
        if not hasattr(self, 'id'):    
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """str method that returns a string representation of an object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Public instance method that updates updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        for attr in ['created_at', 'updated_at']:
            if hasattr(self, attr) and isinstance(getattr(self, attr), datetime):
                dict_copy[attr] = getattr(self, attr).isoformat()
        return dict_copy
