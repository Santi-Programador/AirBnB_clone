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


class TestAmenity(unittest.TestCase):
    """TestAmenity: to test Amenity Class"""
    def test_saveMethod(self):
        """ Function: test_saveMethod
                      to test save instance method
        """
        x = Amenity()
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_to_dict_method(self):
        """ Function: test_to_dict_method
                      to test to_dict instance method
        """
        y = Amenity()
        AmenityDict = y.to_dict()
        self.assertEqual(y.__class__.__name__, 'Amenity')
        self.assertIsInstance(AmenityDict['created_at'], str)
        self.assertIsInstance(AmenityDict['updated_at'], str)
        self.assertIsInstance(AmenityDict['id'], str)

    def test_has_methods(self):
        """ Function: test_attribs
                      to test if have all methods available
        """
        w = Amenity()
        self.assertTrue(hasattr(w, "__init__"))
        self.assertTrue(hasattr(w, "__str__"))
        self.assertTrue(hasattr(w, "save"))
        self.assertTrue(hasattr(w, "to_dict"))

    def test_has_atribs(self):
        """ Function: test_hasaattribs
                      to test if have all basics attribs available
        """
        z = Amenity()
        self.assertTrue(hasattr(z, "name"))
        self.assertTrue("id" in z.__dict__)
        self.assertTrue("created_at" in z.__dict__)
        self.assertTrue("updated_at" in z.__dict__)

    def test_init(self):
        """ Function: test_init
                      to test Amenity Class
        """
        w = Amenity()
        self.assertTrue(isinstance(w, Amenity))
        self.assertIsInstance(w, Amenity)

    def test_str(self):
        """Tests instance's string representation"""
        z = Amenity()
        stringA = str(z)
        stringB = z.__str__()
        self.assertTrue(stringA, stringB)

    def test_types(self):
        """Tests attribute name"""
        i = Amenity()
        self.assertEqual(type(i.name), str)

    def test_inherit(self):
        """Tests inheritance"""
        j = Amenity()
        self.assertTrue(issubclass(j.__class__, BaseModel), True)


if __name__ == "__main__":
    unittest.main()
