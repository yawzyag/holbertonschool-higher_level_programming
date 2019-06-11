import unittest
import pep8
from models.rectangle import Rectangle


class TestStringMethods(unittest.TestCase):
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/rectangle.py"
        file2 = "tests/test_models/test_rectangle.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestRectangleClass(unittest.TestCase):
    """
    Test id

    Test width

    Test height

    Test x

    Test Y

    Test area

    Test str

    Test dictionary

    Test errors

    Test update

    Test kwars
    """
    pass
