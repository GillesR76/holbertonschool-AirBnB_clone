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
        objects_dict = {}
        for key in self.__objects:
            objects_dict[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """reload method"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    obj = eval("{}".format(class_name))
                    for k, v in value.items():
                        if k != '__class__':
                            setattr(obj, k, v)
                    self.__objects[key] = obj
        except Exception as e:
            pass
        """except Exception:
            print("error")
            pass"""
