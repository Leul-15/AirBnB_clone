#!/usr/bin/python3
"""Defines unittests
"""
import unittest
from models.base_model import BaseModel
from time import sleep


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests instantiation of the BaseModel class."""

    def test_two_model_unique_id(self):
        basem1 = BaseModel()
        basem2 = BaseModel()
        self.assertNotEqual(basem1.id, basem2.id)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_init(self):
        basem = BaseModel()
        self.assertIsNotNone(basem.id)
        self.assertIsNotNone(basem.created_at)
        self.assertIsNotNone(basem.updated_at)

    def test_args_unused(self):
        basem = BaseModel(None)
        self.assertNotIn(None, basem.__dict__.values())

    def test_two_models_different_updated_at(self):
        my_model1 = BaseModel()
        sleep(0.05)
        my_model2 = BaseModel()
        self.assertLess(my_model1.updated_at, my_model2.updated_at)

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))


class TestBaseModel_save(unittest.TestCase):
    """Unittests save method of the BaseModel class."""

    def test_save_initial_update_and_current_update_at(self):
        basem = BaseModel()
        init_updated_time = basem.updated_at
        c_updated_time = basem.save()
        self.assertNotEqual(init_updated_time, c_updated_time)

    def test_one_save(self):
        my_model = BaseModel()
        sleep(0.05)
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertLess(initial_updated_at, my_model.updated_at)

    def test_two_saves(self):
        basem = BaseModel()
        sleep(0.05)
        first_updated_at = basem.updated_at
        basem.save()
        second_updated_at = basem.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        basem.save()
        self.assertLess(second_updated_at, basem.updated_at)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests to_dict method of the BaseModel class."""

    def test_to_dict(self):
        basem = BaseModel()
        basem_dict = basem.to_dict()
        self.assertIsInstance(basem_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        basem = BaseModel()
        basem_dict = basem.to_dict()
        self.assertEqual(basem_dict["__class__"], "BaseModel")
        self.assertEqual(basem_dict["id"], basem.id)
        self.assertEqual(basem_dict["created_at"],
                         basem.created_at.isoformat())
        self.assertEqual(basem_dict["updated_at"],
                         basem.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
