#!/usr/bin/python3
"""
Testing BaseModel
"""
from datetime import datetime
import inspect
import models
import pep8 as pycodestyle
import time
import unittest
from unittest import mock
from models import base_model
import os

BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Checking documentation and BaseModel class style"""

    @classmethod
    def setUpClass(cls):
        """
        Setup for Docstring test
        """
        cls.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance(self):
        """Checking that base_model.py conforms to PEP8"""
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Checking for docstring in module"""
        self.assertIsNot(module_doc, None,
                         "docstring not found in base_model.py")
        self.assertTrue(len(module_doc) > 0,
                        "docstring not found in base_model.py")

    def test_class_docstring(self):
        """Checking class docstring in BaseModel"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """Checking docstrings in BaseModel methods"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


class TestBaseModel(unittest.TestCase):
    """TestBaseModel: to test BaseModel Class"""
    def test_filenotexist(self):
        a = BaseModel()
        del a
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

        self.assertTrue(os.access('models/base_model.py', os.R_OK))
        self.assertTrue(os.access('models/base_model.py', os.W_OK))
        self.assertTrue(os.access('models/base_model.py', os.X_OK))

    def test_save_Method(self):
        """ Function: test_save_Method
                      to test save instance method
        """
        x = BaseModel()
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)
        x2 = BaseModel()
        x2.save()
        self.assertNotEqual(x2.created_at, x2.updated_at)
        self.assertNotEqual(x.updated_at, x2.updated_at)

    def test_to_dict_Method(self):
        """ Function: test_to_dict_Method
                      to test to_dict instance method
        """
        y = BaseModel()
        BaseDict = y.to_dict()
        self.assertEqual(y.__class__.__name__, 'BaseModel')
        self.assertIsInstance(BaseDict['created_at'], str)
        self.assertIsInstance(BaseDict['updated_at'], str)
        self.assertIsInstance(BaseDict['id'], str)

    def test_attribs(self):
        """ Function: test_attribs
                      to test if have all methods available
        """
        i = BaseModel()
        self.assertTrue(hasattr(i, "__init__"))
        self.assertTrue(hasattr(i, "__str__"))
        self.assertTrue(hasattr(i, "save"))
        self.assertTrue(hasattr(i, "to_dict"))

    def test_init(self):
        """ Function: test_init
                      to test BaseModel Class
        """
        w = BaseModel()
        self.assertTrue(isinstance(w, BaseModel))
        self.assertIsInstance(w, BaseModel)

    def test_str(self):
        """ Function: test_str
                      to test BaseModel Class
        """
        z = BaseModel()
        stringA = str(z)
        stringB = z.__str__()
        self.assertTrue(stringA, stringB)

        stringA = "[BaseModel] ({}) {}".format(z.id, z.__dict__)
        stringB = str(z)
        self.assertEqual(stringA, stringB)

if __name__ == "__main__":
    unittest.main()
