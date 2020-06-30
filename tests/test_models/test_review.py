#!/usr/bin/python3
"""
Testing review
"""

from datetime import datetime
import inspect
from models import review
from models.base_model import BaseModel
import pep8
import unittest
Review = review.Review


class TestReviewDocs(unittest.TestCase):
    """Checking documentation and Review class style"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.review_f = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_review(self):
        """Checking that review.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors in review.py")

    def test_pep8_conformance_test_review(self):
        """Checking that test_review.py conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors in test_review.py")

    def test_review_module_docstring(self):
        """Checking for Review class docstring"""
        self.assertIsNot(review.__doc__, None,
                         "docstring module not found in review.py")
        self.assertTrue(len(review.__doc__) >= 1,
                        "docstring module not found in review.py")

    def test_review_class_docstring(self):
        """Checking for the Review class docstring"""
        self.assertIsNot(Review.__doc__, None,
                         "docstring not found in Review class")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "docstring not found in Review class")

    def test_review_func_docstrings(self):
        """Test for the presence of docstrings in Review methods"""
        for func in self.review_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method failed in docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method failed in docstring".format(func[0]))
