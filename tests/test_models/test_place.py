#!/usr/bin/python3
"""
Testing place
"""

from datetime import datetime
import inspect
from models import place
from models.base_model import BaseModel
import pep8
import unittest
Place = place.Place


class TestPlaceDocs(unittest.TestCase):
    """Checking documentation and Place class style"""
    @classmethod
    def setUpClass(cls):
        """
        Set up for the doc tests
        """
        cls.place_f = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_conformance_place(self):
        """Checking that models/place.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors in place.py")

    def test_pep8_conformance_test_place(self):
        """Checking that test_place.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors in test_place.py")

    def test_place_module_docstring(self):
        """Checking for Place class docstring"""
        self.assertIsNot(place.__doc__, None,
                         "docstring module not found in place.py")
        self.assertTrue(len(place.__doc__) >= 1,
                        "docstring module not found in place.py")

    def test_place_class_docstring(self):
        """Checking for the Place class docstring"""
        self.assertIsNot(Place.__doc__, None,
                         "docstring not found in Place class")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "docstring not found in Place class")

    def test_place_func_docstrings(self):
        """Checking docstrings in Place methods"""
        for func in self.place_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method failed in docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method failed in docstring".format(func[0]))
