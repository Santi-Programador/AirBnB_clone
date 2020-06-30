#!/usr/bin/python3
"""
Testing state
"""

from datetime import datetime
import inspect
from models import state
from models.base_model import BaseModel
import pep8
import unittest
State = state.State


class TestStateDocs(unittest.TestCase):
    """Checking documentation and Review class style"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.state_f = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_state(self):
        """Checking that state.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors in state.py")

    def test_pep8_conformance_test_state(self):
        """Checking that test_state.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors in state.py.")

    def test_state_module_docstring(self):
        """Checking for State class docstring"""
        self.assertIsNot(state.__doc__, None,
                         "docstring module not found in state.py")
        self.assertTrue(len(state.__doc__) >= 1,
                        "docstring module not found in state.py")

    def test_state_class_docstring(self):
        """Checking for the State class docstring"""
        self.assertIsNot(State.__doc__, None,
                         "docstring not found in State class")
        self.assertTrue(len(State.__doc__) >= 1,
                        "docstring not found in State class")

    def test_state_func_docstrings(self):
        """Test for the presence of docstrings in State methods"""
        for func in self.state_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method failed in docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method failed in docstring".format(func[0]))
