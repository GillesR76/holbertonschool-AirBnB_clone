#!/usr/bin/python3


"""
* Write a class FileStorage that serializes instances to
a JSON file and deserializes JSON file to instances:

* Private class attributes:
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by <class name>.id

* Public instance methods:
    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key <obj class name>.id
    save(self): serializes __objects to the JSON file (path: __file_path)
    reload(self): deserializes the JSON file to __objects
    (only if the JSON file
"""

import json
import os

class FileStorage:
    """
    class Filestorage
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Method all
        """
        return self.__objects

    def new(self, obj):
        """
        New method
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        save method
        """
        objects_dict = dict({})
        for (key, value) in self.__objects.items():
            objects_dict[key] = value.to_dict()
        try:
            with open(self.__file_path, 'w', encoding="utf-8") as file:
                json.dump(objects_dict, file)
        except:
            pass

    def reload(self):
        """reload method"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        if not os.path.exists(self.__file_path):
            return
        try:
            with open(self.__file_path, 'r') as file:
                if os.path.getsize(self.__file_path) == 0:
                    return
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except (FileNotFoundError):
            pass
