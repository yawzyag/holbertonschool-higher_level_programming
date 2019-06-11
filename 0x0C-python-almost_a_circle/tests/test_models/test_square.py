import unittest
import pep8
from models.square import Square


class TestStringMethods(unittest.TestCase):
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/square.py"
        file2 = "tests/test_models/test_square.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestSquareClass(unittest.TestCase):
    """
    Set up class

    Test id

    Test size

    Test x

    Test y

    Test area

    Test str

    Test dictionary

    Test errors

    Test update

    Test kwars
    """
    def setUp(self):
        self.s1 = Square(5)
        self.s2 = Square(2, 2)
        self.s3 = Square(3, 1, 3)

    def tearDown(self):
        pass

    def test_id(self):
        self.assertEqual(self.s1.id, 21)
