#!/usr/bin/python3
"""Defines unittests
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests instantiation of the City class"""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_name_is_public_class_attribute(self):
        cit = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cit))
        self.assertNotIn("name", cit.__dict__)

    def test_two_cities_unique_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests save method of the City class"""

    def test_one_save(self):
        cit = City()
        sleep(0.05)
        first_updated_at = cit.updated_at
        cit.save()
        self.assertLess(first_updated_at, cit.updated_at)

    def test_save_with_arg(self):
        cit = City()
        with self.assertRaises(TypeError):
            cit.save(None)


class TestCity_to_dict(unittest.TestCase):
    """Unittests to_dict method of the City class"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        cit = City()
        self.assertIn("id", cit.to_dict())
        self.assertIn("created_at", cit.to_dict())
        self.assertIn("updated_at", cit.to_dict())
        self.assertIn("__class__", cit.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        cit = City()
        city_dict = cit.to_dict()
        self.assertEqual(str, type(city_dict["id"]))
        self.assertEqual(str, type(city_dict["created_at"]))
        self.assertEqual(str, type(city_dict["updated_at"]))

    def test_contrast_to_dict_dunder_dict(self):
        cit = City()
        self.assertNotEqual(cit.to_dict(), cit.__dict__)

    def test_to_dict_with_arg(self):
        cit = City()
        with self.assertRaises(TypeError):
            cit.to_dict(None)


if __name__ == "__main__":
    unittest.main()
