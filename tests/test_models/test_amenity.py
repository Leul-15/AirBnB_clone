#!/usr/bin/python3
"""
Defines unittests
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests instantiation of the Amenity class"""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_two_amenities_unique_ids(self):
        amenit1 = Amenity()
        amenit2 = Amenity()
        self.assertNotEqual(amenit1.id, amenit2.id)


class TestAmenity_save(unittest.TestCase):
    """Unittests save method of the Amenity class"""

    def test_one_save(self):
        amenit = Amenity()
        sleep(0.05)
        first_updated_at = amenit.updated_at
        amenit.save()
        self.assertLess(first_updated_at, amenit.updated_at)

    def test_save_with_arg(self):
        amenit = Amenity()
        with self.assertRaises(TypeError):
            amenit.save(None)


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests to_dict method of the Amenity class"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amenit = Amenity()
        self.assertIn("id", amenit.to_dict())
        self.assertIn("created_at", amenit.to_dict())
        self.assertIn("updated_at", amenit.to_dict())
        self.assertIn("__class__", amenit.to_dict())

    def test_contrast_to_dict_dunder_dict(self):
        amenit = Amenity()
        self.assertNotEqual(amenit.to_dict(), amenit.__dict__)

    def test_to_dict_with_arg(self):
        amenit = Amenity()
        with self.assertRaises(TypeError):
            amenit.to_dict(None)

    def test_to_dict_datetime_attributes_are_strs(self):
        amenit = Amenity()
        amenit_dict = amenit.to_dict()
        self.assertEqual(str, type(amenit_dict["id"]))
        self.assertEqual(str, type(amenit_dict["created_at"]))
        self.assertEqual(str, type(amenit_dict["updated_at"]))


if __name__ == "__main__":
    unittest.main()
