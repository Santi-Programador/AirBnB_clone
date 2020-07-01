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


class TestReview(unittest.TestCase):
    """TestReview: to test Review Class"""
    def test_saveMethod(self):
        """ Function: test_saveMethod
                      to test save instance method
        """
        x = Review()
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_to_dict_Method(self):
        """ Function: test_to_dict_Method
                      to test to_dict instance method
        """
        y = Review()
        ReviewDict = y.to_dict()
        self.assertEqual(y.__class__.__name__, 'Review')
        self.assertIsInstance(ReviewDict['created_at'], str)
        self.assertIsInstance(ReviewDict['updated_at'], str)
        self.assertIsInstance(ReviewDict['id'], str)

    def test_has_methods(self):
        """ Function: test_attribs
                      to test if have all methods available
        """
        w = Review()
        self.assertTrue(hasattr(w, "__init__"))
        self.assertTrue(hasattr(w, "__str__"))
        self.assertTrue(hasattr(w, "save"))
        self.assertTrue(hasattr(w, "to_dict"))

    def test_has_atribs(self):
        """ Function: test_has_aattribs
                      to test if have all basics attribs available
        """
        z = Review()
        self.assertTrue(hasattr(z, "place_id"))
        self.assertTrue(hasattr(z, "user_id"))
        self.assertTrue(hasattr(z, "text"))
        self.assertTrue(hasattr(z, "created_at"))
        self.assertTrue(hasattr(z, "updated_at"))
        self.assertTrue("id" in z.__dict__)
        self.assertTrue("created_at" in z.__dict__)
        self.assertTrue("updated_at" in z.__dict__)

    def test_init(self):
        """ Function: test_init
                      to test Review Class
        """
        w = Review()
        self.assertTrue(isinstance(w, Review))
        self.assertIsInstance(w, Review)

    def test_str(self):
        z = Review()
        stringA = str(z)
        stringB = z.__str__()
        self.assertTrue(stringA, stringB)

    def test_types(self):
        i = Review()
        self.assertEqual(type(i.place_id), str)
        self.assertEqual(type(i.user_id), str)
        self.assertEqual(type(i.text), str)

    def test_inherit(self):
        j = Review()
        self.assertTrue(issubclass(j.__class__, BaseModel), True)

if __name__ == "__main__":
    unittest.main()
