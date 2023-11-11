#!/usr/bin/python3
"""
class BaseModel that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, tform))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute 
        updated_at with the 
        current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values 
        of __dict__ of the instance
        """
        in_dict = self.__dict__.copy()
        in_dict["__class__"] = self.__class__.__name__
        in_dict["created_at"] = self.created_at.isoformat()
        in_dict["updated_at"] = self.updated_at.isoformat()

        return in_dict

    def __str__(self):
        """
        Return the str representation of the BaseModel instance
        """
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
