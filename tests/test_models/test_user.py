#!/usr/bin/python3
"""
Defines unittests
"""
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser_instantiation(unittest.TestCase):
    """Unittests instantiation of the User class."""

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)


class TestUser_save(unittest.TestCase):
    """Unittests save method of the  class."""

    def test_save_with_arg(self):
        user1 = User()
        with self.assertRaises(TypeError):
            user1.save(None)

    def test_save_updates_file(self):
        user1 = User()
        user1.save()
        user_id = "User." + user1.id
        with open("file.json", "r") as f:
            self.assertIn(user_id, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        user1 = User()
        self.assertIn("id", user1.to_dict())
        self.assertIn("created_at", user1.to_dict())
        self.assertIn("updated_at", user1.to_dict())
        self.assertIn("__class__", user1.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        user1 = User()
        user_dict = user1.to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_contrast_to_dict_dunder_dict(self):
        user1 = User()
        self.assertNotEqual(user1.to_dict(), user1.__dict__)


if __name__ == "__main__":
    unittest.main()
