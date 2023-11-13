#!/usr/bin/python3
"""
program called console that contains the entry point of the
command interpreter
"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    class definition
    """
    prompt = "(hbnb) "
    class_name = ["BaseModel", "User", "State",
                  "City", "Place", "Amenity", "Review"]

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self):
        """
        Display help for the quit command
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Exit the program on EOF
        """
        print()
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """
        Create a new class instance and print its id.
        """
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.class_name:
            print("** class doesn't exist **")
        else:
            basem = eval(f"{cmds[0]}()")
            storage.save()
            print(basem.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.class_name:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = "{}.{}".format(cmds[0], cmds[1])
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.class_name:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = "{}.{}".format(cmds[0], cmds[1])
            if key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on
        the class name
        """
        obj = storage.all()
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            for key, value in obj.items():
                print(str(value))
        elif cmds[0] not in self.class_name:
            print("** class doesn't exist **")
        else:
            for k, v in obj.items():
                if k.split(".")[0] == cmds[0]:
                    print(str(v))

    def default(self, arg):
        """
        Default method
        """
        cmd_list = arg.split(".")
        cls_name = cmd_list[0]
        cmds = cmd_list[1].split("(")
        new_cmds = cmds[0]
        new_arg = cmds[1].split(")")[0]
        new_dict = {
            "show": self.do_show,
            "all": self.do_all,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }
        if new_cmds in new_dict.keys():
            return new_dict[new_cmds]("{} {}".format(cls_name, new_arg))
        print(" Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """
        to retrieve the number of instances of a class
        """
        objs = storage.all()
        cmds = shlex.split(arg)
        if arg:
            new_cls_name = cmds[0]
        count = 0
        if cmds:
            if new_cls_name in self.class_name:
                for obj in objs.values():
                    if obj.__class__.__name__ == new_cls_name:
                        count += 1
                print(count)
            else:
                print("** Invalid class name **")
        else:
            print("** Unknown syntax **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        """
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.class_name:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = "{}.{}".format(cmds[0], cmds[1])
            if key not in obj:
                print("** no instance found **")
            elif len(cmds) < 3:
                print("** attribute name missing **")
            elif len(cmds) < 4:
                print("** value missing **")
            else:
                objects = obj[key]
                attribute_name = cmds[2]
                attribute_value = cmds[3]

                try:
                    attribute_value = eval(attribute_value)
                except Exception:
                    pass
                setattr(objects, attribute_name, attribute_value)
                objects.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
