#!/usr/bin/python3
"""
Testing amenity.py
"""

from datetime import datetime
import inspect
from models import amenity
from models.base_model import BaseModel
import pep8
import unittest
Amenity = amenity.Amenity


class TestAmenityDocs(unittest.TestCase):
    """
    Checking documentation and Amenity class style
    """
    @classmethod
    def setUpClass(cls):
        """
        Setup for Docstring test
        """
        cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        """Checking that amenity.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors")

    def test_pep8_conformance_test_amenity(self):
        """Checking test_amenity.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors in test_amenity")

    def test_amenity_module_docstring(self):
        """Checking for the amenity.py module docstring"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "docstring module not found in amenity.py")

    def test_amenity_class_docstring(self):
        """Checking for the Amenity class docstring"""
        self.assertIsNot(Amenity.__doc__, None,
                         "docstring not found in Amenity class")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "docstring not found in Amenity class")

    def test_amenity_func_docstrings(self):
        """Checking docstrings in Amenity methods"""
        for func in self.amenity_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method failed in docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method failed in docstring".format(func[0]))
