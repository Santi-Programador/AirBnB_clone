#!/usr/bin/python3
"""
Testing User
"""

from datetime import datetime
import inspect
from models import user
from models.base_model import BaseModel
import pep8
import unittest
User = user.User


class TestUserDocs(unittest.TestCase):
    """Checking documentation and User class style"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Checking that user.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors in user.py")

    def test_pep8_conformance_test_user(self):
        """Checking that test_user.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors in test_user.py")

    def test_user_module_docstring(self):
        """Checking for User class docstring"""
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "docstring module not found in user.py")

    def test_user_class_docstring(self):
        """Checking for the User class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "docstring not found in User class")
        self.assertTrue(len(User.__doc__) >= 1,
                        "docstring not found in User class")

    def test_user_func_docstrings(self):
        """Test for the presence of docstrings in User methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method failed in docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method failed in docstring".format(func[0]))


class TestUser(unittest.TestCase):
    """TestUser: to test User Class"""
    def test_save_Method(self):
        """ Function: test_saveMethod
                      to test save instance method
        """
        x = User()
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_to_dict_Method(self):
        """ Function: test_to_dictMethod
                      to test to_dict instance method
        """
        y = User()
        UserDict = y.to_dict()
        self.assertEqual(y.__class__.__name__, 'User')
        self.assertIsInstance(UserDict['created_at'], str)
        self.assertIsInstance(UserDict['updated_at'], str)
        self.assertIsInstance(UserDict['id'], str)

    def test_has_methods(self):
        """ Function: test_attribs
                      to test if have all methods available
        """
        w = User()
        self.assertTrue(hasattr(w, "__init__"))
        self.assertTrue(hasattr(w, "__str__"))
        self.assertTrue(hasattr(w, "save"))
        self.assertTrue(hasattr(w, "to_dict"))

    def test_hasatribs(self):
        """ Function: test_hasaattribs
                      to test if have all basics attribs available
        """
        z = User()
        self.assertTrue(hasattr(z, "email"))
        self.assertTrue(hasattr(z, "password"))
        self.assertTrue(hasattr(z, "last_name"))
        self.assertTrue(hasattr(z, "first_name"))
        self.assertTrue(hasattr(z, "created_at"))
        self.assertTrue(hasattr(z, "updated_at"))
        self.assertTrue("id" in z.__dict__)
        self.assertTrue("created_at" in z.__dict__)
        self.assertTrue("updated_at" in z.__dict__)

    def test_init(self):
        """ Function: test_init
                      to test User Class
        """
        w = User()
        self.assertTrue(isinstance(w, User))
        self.assertIsInstance(w, User)

    def test_str(self):
        z = User()
        stringA = str(z)
        stringB = z.__str__()
        self.assertTrue(stringA, stringB)

    def test_strings(self):
        i = User()
        self.assertEqual(type(i.email), str)
        self.assertEqual(type(i.password), str)
        self.assertEqual(type(i.first_name), str)
        self.assertEqual(type(i.first_name), str)

    def test_inherit(self):
        j = User()
        self.assertTrue(issubclass(j.__class__, BaseModel), True)

if __name__ == "__main__":
    unittest.main()
