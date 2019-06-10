import unittest
import pep8
from models import base


class TestStringMethods(unittest.TestCase):
    def testep8(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/base.py"
        file2 = "tests/test_models/test_base.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")

    
