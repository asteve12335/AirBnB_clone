#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
from os import path


class FileStorage:

    """Class for storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                input = json.load(f)
                for k, v in input.items():
                    FileStorage.__objects[k] = eval(v["__class__"])(**v)
        else:
            pass
