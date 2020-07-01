#!/usr/bin/python3
"""
Testing file_storage
"""

from datetime import datetime
import inspect
from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
FileStorage = file_storage.FileStorage
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_file_storage(self):
        """Test that models/engine/file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """Test tests/test_models/test_file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_file_storage_module_docstring(self):
        """Test for the file_storage.py module docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py needs a docstring")

    def test_file_storage_class_docstring(self):
        """Test for the FileStorage class docstring"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "State class needs a docstring")

    def test_fs_func_docstrings(self):
        """Test for the presence of docstrings in FileStorage methods"""
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """TestFileStorage: to test FileStorage Class"""
    @classmethod
    def setUpClass(cls):
        """
        set storage variable to test
        """
        cls.storage = FileStorage()

    def test_filestoragepyfile(self):
        """test file file_storage.py permissions file"""
        self.assertTrue(os.access('models/engine/file_storage.py', os.R_OK))
        self.assertTrue(os.access('models/engine/file_storage.py', os.W_OK))
        self.assertTrue(os.access('models/engine/file_storage.py', os.X_OK))

    def test_all(self):
        """Test return dictionary __objects"""
        storage = FileStorage()
        dictionary = storage.all()
        self.assertIsNotNone(dictionary)
        self.assertEqual(type(dictionary), dict)
        self.assertIs(dictionary, storage._FileStorage__objects)

    def test_new(self):
        """Test if saves object into dictionary"""
        storage = FileStorage()
        dictionary = storage.all()
        x = User()
        x.id = "56d43177-cc5f-4d6c-a0c1-e167f8c27337"
        x.name = "Winston Smith"
        storage.new(x)
        key = x.__class__.__name__ + "." + str(x.id)
        self.assertIsNotNone(dictionary[key])

    def test_reload(self):
        """Test if reloads objects from json file in dictionary"""
        self.storage.save()
        path = os.path.dirname(os.path.abspath("console.py"))
        fd = os.path.join(path, "file.json")
        with open(fd, 'r') as f:
            lines = f.readlines()

        try:
            os.remove(pt)
        except BaseException:
            pass

        self.storage.save()

        with open(fd, 'r') as f:
            lines2 = f.readlines()

        self.assertEqual(lines, lines2)

        try:
            os.remove(pt)
        except BaseException:
            pass

        with open(fd, "w") as f:
            f.write("{}")
        with open(fd, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")

        self.assertIs(self.storage.reload(), None)

if __name__ == "__main__":
    unittest.main()
