#!/usr/bin/python3
"""
program called console that contains the entry point of the
command interpreter
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    class definition
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self, arg):
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
