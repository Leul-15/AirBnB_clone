#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
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
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file, indent=2)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        c_name, oid = key.split(".")
                        c = eval(c_name)
                        inst = c(**value)
                        FileStorage.__objects[key] = inst
                except FileNotFoundError:
                    return
