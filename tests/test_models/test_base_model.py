import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test the functionality of the BaseModel class"""

    def setUp(self):
        """Set up the tests"""
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_init(self):
        """Test the initialization of the BaseModel class"""
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_save(self):
        """Test the save method of the BaseModel class"""
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel class"""
        model_dict = self.my_model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.my_model.id)
        self.assertEqual(model_dict["name"], "My First Model")
        self.assertEqual(model_dict["my_number"], 89)
        self.assertEqual(model_dict["created_at"], self.my_model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.my_model.updated_at.isoformat())

    def test_str(self):
        """Test the __str__ method of the BaseModel class"""
        model_str = self.my_model.__str__()
        expected_str = f"[BaseModel] ({self.my_model.id}) {self.my_model.to_dict()}"
        self.assertEqual(model_str, expected_str)

if __name__ == '__main__':
    unittest.main()