import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test the functionality of the FileStorage class
    """
    def setUp(self):
        """Set up the tests"""
        self.storage = FileStorage()
        self.model = BaseModel()
        print(self.storage._FileStorage__objects)

    def test_all(self):
        """
        Test the all method of the FileStorage class
        """
        # Test if all returns a dictionary
        self.assertEqual(type(self.storage.all()), dict)

        # Test if all returns the correct dictionary
        self.storage.new(self.model)
        self.assertEqual(
            self.storage.all(),
            self.storage._FileStorage__objects
        )

    def test_new(self):
        """
        Test the new method of the FileStorage class
        """
        # Test if new adds an object to __objects
        self.storage.new(self.model)
        key = self.model.__class__.__name__ + "." + self.model.id
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """
        Test the save method of the FileStorage class
        """
        # Test if save creates a file
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

        with open('file.json', 'r') as file:
            self.assertIn("BaseModel." + self.model.id, json.load(file))

    def test_reload(self):
        """
        Test the reload method of the FileStorage class
        """
        # Test if reload reads from a file
        self.assertTrue(os.path.exists("file.json"))
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        self.assertIn("BaseModel." + self.model.id, self.storage.all())
        with open('file.json', 'r') as file:
            self.assertIn("BaseModel." + self.model.id, json.load(file))


if __name__ == '__main__':
    unittest.main()
