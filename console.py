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
    prompt = "(hbnb)"
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
