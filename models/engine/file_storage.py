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

class FileStorage:
    
    