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
