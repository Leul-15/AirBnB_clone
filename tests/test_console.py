#!/usr/bin/python3
"""
Defines unittests
"""
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests prompting of the command interpreter"""

    def test_prompt_string(self):
        self.assertEqual("(hbnb)", HBNBCommand.prompt)


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests help messages of the command interpreter"""

    def test_help_quit(self):
        text = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(text, output.getvalue().strip())


class TestHBNBCommand_exit(unittest.TestCase):
    """Unittests exiting from the command interpreter"""

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))


class TestHBNBCommand_create(unittest.TestCase):
    """Unittests create from the command interpreter"""

    def test_create_missing_class(self):
        text = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(text, output.getvalue().strip())


class TestHBNBCommand_show(unittest.TestCase):
    """Unittests show from the command interpreter"""

    def test_show_missing_class(self):
        text = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(text, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(text, output.getvalue().strip())


class TestHBNBCommand_destroy(unittest.TestCase):
    """Unittests destroy from the command interpreter"""

    def test_destroy_missing_class(self):
        text = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(text, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".destroy()"))
            self.assertEqual(text, output.getvalue().strip())


class TestHBNBCommand_all(unittest.TestCase):
    """Unittests all of the command interpreter"""

    def test_all_invalid_class(self):
        text = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(text, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.all()"))
            self.assertEqual(text, output.getvalue().strip())


class TestHBNBCommand_update(unittest.TestCase):
    """Unittests update from the command interpreter"""

    def test_update_missing_class(self):
        text = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(text, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".update()"))
            self.assertEqual(text, output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
