#!/usr/bin/python3
"""Unittests
"""
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests FileStorage class"""

    def test_all_storage_returns_dictionary(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        basem = BaseModel()
        models.storage.new(basem)
        self.assertIn("BaseModel.{}".format(basem.id), models.storage.all())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)


if __name__ == "__main__":
    unittest.main()
