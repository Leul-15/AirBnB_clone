#!/usr/bin/python3
"""Defines the FileStorage class"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file and 
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        obj_cls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_cls_name, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        all_objs = FileStorage.__objects
        obj_dict = {obj: all_objs[obj].to_dict() for obj in all_objs.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file, indent=2)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        file_name = FileStorage.__file_path
        if (not os.path.exists(file_name)) or os.stat(file_name).st_size == 0:
            return

        class_name = {"Amenity": Amenity,
                      "BaseModel": BaseModel,
                      "City": City,
                      "Place": Place,
                      "Review": Review,
                      "State": State,
                      "User": User}
        with open(FileStorage.__file_path, "r") as file:
            obj_dict = json.load(file)
        for key, value in obj_dict.items():
            if value['__class__'] in class_name.keys():
                value = class_name[key.split(".")[0]](**value)
                FileStorage.__objects.update({key: value})
            else:
                print("** class doesn't exist **")
                FileStorage.__objects.update({key: None})
