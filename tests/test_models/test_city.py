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


class TestCity(unittest.TestCase):
    """TestCity: to test City Class"""
    def test_save_Method(self):
        """ Function: test_saveMethod
                      to test save instance method
        """
        x = City()
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_to_dict_Method(self):
        """ Function: test_to_dictMethod
                      to test to_dict instance method
        """
        y = City()
        CityDict = y.to_dict()
        self.assertEqual(y.__class__.__name__, 'City')
        self.assertIsInstance(CityDict['created_at'], str)
        self.assertIsInstance(CityDict['updated_at'], str)
        self.assertIsInstance(CityDict['id'], str)

    def test_has_methods(self):
        """ Function: test_attribs
                      to test if have all methods available
        """
        w = City()
        self.assertTrue(hasattr(w, "__init__"))
        self.assertTrue(hasattr(w, "__str__"))
        self.assertTrue(hasattr(w, "save"))
        self.assertTrue(hasattr(w, "to_dict"))

    def test_hasatribs(self):
        """ Function: test_hasaattribs
                      to test if have all basics attribs available
        """
        z = City()
        self.assertTrue(hasattr(z, "name"))
        self.assertTrue(hasattr(z, "state_id"))
        self.assertTrue("id" in z.__dict__)
        self.assertTrue("created_at" in z.__dict__)
        self.assertTrue("updated_at" in z.__dict__)

    def test_init(self):
        """ Function: test_init
                      to test CityClass
        """
        w = City()
        self.assertTrue(isinstance(w, City))
        self.assertIsInstance(w, City)

    def test_str(self):
        z = City()
        stringA = str(z)
        stringB = z.__str__()
        self.assertTrue(stringA, stringB)

    def test_types(self):
        i = City()
        self.assertEqual(type(i.name), str)
        self.assertEqual(type(i.state_id), str)

    def test_inherit(self):
        j = City()
        self.assertTrue(issubclass(j.__class__, BaseModel), True)

if __name__ == "__main__":
    unittest.main()
