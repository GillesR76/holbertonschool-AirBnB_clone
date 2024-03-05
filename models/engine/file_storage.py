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
    reload(self): deserializes the JSON file to __objects (only if the JSON file
"""

import json
from os.path import exists

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
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj.to_dict()
    
    def save(self):
        """
        save method
        """
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(self.__objects, file)
    
    def reload(self):
        """reload method"""
        if not exists(self.__file_path):
            return
        
        with open(self.__file_path, 'r', encoding="utf-8") as file:
            return json.load(file)