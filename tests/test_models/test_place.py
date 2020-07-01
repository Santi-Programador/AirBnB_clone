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


class TestPlace(unittest.TestCase):
    """TestPlace: to test Place Class"""
    def test_save_Method(self):
        """ Function: test_saveMethod
                      to test save instance method
        """
        x = Place()
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_to_dict_Method(self):
        """ Function: test_to_dictMethod
                      to test to_dict instance method
        """
        y = Place()
        PlaceDict = y.to_dict()
        self.assertEqual(y.__class__.__name__, 'Place')
        self.assertIsInstance(PlaceDict['created_at'], str)
        self.assertIsInstance(PlaceDict['updated_at'], str)
        self.assertIsInstance(PlaceDict['id'], str)

    def test_has_methods(self):
        """ Function: test_attribs
                      to test if have all methods available
        """
        w = Place()
        self.assertTrue(hasattr(w, "__init__"))
        self.assertTrue(hasattr(w, "__str__"))
        self.assertTrue(hasattr(w, "save"))
        self.assertTrue(hasattr(w, "to_dict"))

    def test_hasatribs(self):
        """ Function: test_hasaattribs
                      to test if have all basics attribs available
        """
        z = Place()
        self.assertTrue(hasattr(z, "city_id"))
        self.assertTrue(hasattr(z, "user_id"))
        self.assertTrue(hasattr(z, "name"))
        self.assertTrue(hasattr(z, "description"))
        self.assertTrue(hasattr(z, "number_rooms"))
        self.assertTrue(hasattr(z, "number_bathrooms"))
        self.assertTrue(hasattr(z, "number_bathrooms"))
        self.assertTrue(hasattr(z, "price_by_night"))
        self.assertTrue(hasattr(z, "latitude"))
        self.assertTrue(hasattr(z, "longitude"))
        self.assertTrue(hasattr(z, "amenity_ids"))
        self.assertTrue(hasattr(z, "created_at"))
        self.assertTrue(hasattr(z, "updated_at"))
        self.assertTrue("id" in z.__dict__)
        self.assertTrue("created_at" in z.__dict__)
        self.assertTrue("updated_at" in z.__dict__)

    def test_init(self):
        """ Function: test_init
                      to test Place Class
        """
        w = Place()
        self.assertTrue(isinstance(w, Place))
        self.assertIsInstance(w, Place)

    def test_str(self):
        z = Place()
        stringA = str(z)
        stringB = z.__str__()
        self.assertTrue(stringA, stringB)

    def test_strings(self):
        i = Place()
        self.assertEqual(type(i.city_id), str)
        self.assertEqual(type(i.user_id), str)
        self.assertEqual(type(i.name), str)
        self.assertEqual(type(i.description), str)
        self.assertEqual(type(i.number_rooms), int)
        self.assertEqual(type(i.number_bathrooms), int)
        self.assertEqual(type(i.max_guest), int)
        self.assertEqual(type(i.price_by_night), int)
        self.assertEqual(type(i.latitude), float)
        self.assertEqual(type(i.longitude), float)
        self.assertEqual(type(i.amenity_ids), list)

    def test_inherit(self):
        j = Place()
        self.assertTrue(issubclass(j.__class__, BaseModel), True)

if __name__ == "__main__":
    unittest.main()
