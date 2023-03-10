#!/usr/bin/env python3
"""
Module that contain a class called FileStorage
FileStorage - Class that serializes instances
to a JSON file and deserializes JSON file to instances
"""
import datetime
import json
import os


class FileStorage():
    """Class that serializes instances to a JSON file
    and deserializes JSON file to instances
    Args:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store
                   all objects by <class name>.id
                   ex: to store a BaseModel object with id=12121212,
                   the key will be BaseModel.12121212)
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects['{}.{}'
                              .format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = FileStorage.__objects.copy()
        output = {k: v.to_dict() for k, v in obj_dict.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(output, f, sort_keys=True, indent=4)
            
    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Reloads the stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            # TODO: should this overwrite or insert?
            FileStorage.__objects = obj_dict
