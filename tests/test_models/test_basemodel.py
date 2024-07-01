#!/usr/bin/python3
"""Test BaseModel for expected behavior and documentation"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
import models

class TestBaseModel(unittest.TestCase):

    def test_init_no_kwargs(self):
        """Test initialization without kwargs."""
        instance = BaseModel()
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    def test_init_with_kwargs(self):
        """Test initialization with kwargs."""
        kwargs = {"id": "123", "created_at": "2021-06-29T15:27:48.789123", "updated_at": "2021-06-29T15:27:48.789123"}
        instance = BaseModel(**kwargs)
        self.assertEqual(instance.id, "123")
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method."""
        instance = BaseModel()
        expected_str = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(instance.__str__(), expected_str)

    def test_save(self):
        """Test the save method."""
        instance = BaseModel()
        with self.assertRaises(NotImplementedError):
            instance.save()

    def test_to_dict(self):
        """Test the to_dict method."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertIsInstance(instance_dict["created_at"], str)
        self.assertIsInstance(instance_dict["updated_at"], str)
        self.assertNotIn("_sa_instance_state", instance_dict)

    def test_delete(self):
        """Test the delete method."""
        instance = BaseModel()
        with self.assertRaises(NotImplementedError):
            instance.delete()

if __name__ == "__main__":
    unittest.main()