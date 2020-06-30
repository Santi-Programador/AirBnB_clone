#!/usr/bin/python3
"""
Testing city.py
"""

from datetime import datetime
import inspect
from models import city
from models.base_model import BaseModel
import pep8
import unittest
City = city.City


class TestCityDocs(unittest.TestCase):
    """Checking documentation and City class style"""
    @classmethod
    def setUpClass(cls):
        """
        Set up for the doc tests
        """
        cls.city_f = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_city(self):
        """Checking that city.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors")

    def test_pep8_conformance_test_city(self):
        """Checking test_city.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors in test_city")

    def test_city_module_docstring(self):
        """Checking for the city.py module docstring"""
        self.assertIsNot(city.__doc__, None,
                         "docstring module not found in city.py")
        self.assertTrue(len(city.__doc__) >= 1,
                        "docstring module not found in city.py")

    def test_city_class_docstring(self):
        """Checking for City class docstring"""
        self.assertIsNot(City.__doc__, None,
                         "docstring not found in City class")
        self.assertTrue(len(City.__doc__) >= 1,
                        "docstring not found in City class")

    def test_city_func_docstrings(self):
        """Checking docstrings in City methods"""
        for func in self.city_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method failed in docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method failed in docstring".format(func[0]))
