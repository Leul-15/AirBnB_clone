#!/usr/bin/python3
"""
program called console that contains the entry point of the
command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
import json
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ class definition """
    prompt = '(hbnb) '
    class_name = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program on EOF
        """
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line"""
        pass

    def do_create(self, arg):
        """
        Create a new class instance and print its id.
        """
        if not arg:
            print("** class name missing **")
            return
        cmds = shlex.split(arg)
        if cmds[0] not in HBNBCommand.class_name.keys():
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.class_name[cmds[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the 
        class name and id
        """
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
            return
        if cmds[0] not in HBNBCommand.class_name.keys():
            print("** class doesn't exist **")
            return
        if len(cmds) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs_dict = storage.all()
        key = cmds[0] + "." + cmds[1]
        if key in objs_dict:
            obj_instance = str(objs_dict[key])
            print(obj_instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
            return
        if cmds[0] not in HBNBCommand.class_name.keys():
            print("** class doesn't exist **")
            return
        if len(cmds) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        obj_dict = storage.all()
        key = cmds[0] + "." + cmds[1]
        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on 
        the class name
        """
        storage.reload()
        json_data = []
        obj_dict = storage.all()
        if not arg:
            for key in obj_dict:
                json_data.append(str(obj_dict[key]))
            print(json.dumps(json_data))
            return
        cmds = shlex.split(arg)
        if cmds[0] in HBNBCommand.class_name.keys():
            for key in obj_dict:
                if cmds[0] in key:
                    json_data.append(str(obj_dict[key]))
            print(json.dumps(json_data))
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and 
        id by adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
            return
        cmds = shlex.split(arg)
        storage.reload()
        obj_dict = storage.all()
        if cmds[0] not in HBNBCommand.class_name.keys():
            print("** class doesn't exist **")
            return
        if (len(cmds) == 1):
            print("** instance id missing **")
            return
        try:
            key = cmds[0] + "." + cmds[1]
            obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(cmds) == 2):
            print("** attribute name missing **")
            return
        if (len(cmds) == 3):
            print("** value missing **")
            return
        new_instance = obj_dict[key]
        if hasattr(new_instance, cmds[2]):
            data_type = type(getattr(new_instance, cmds[2]))
            setattr(new_instance, cmds[2], data_type(cmds[3]))
        else:
            setattr(new_instance, cmds[2], cmds[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
