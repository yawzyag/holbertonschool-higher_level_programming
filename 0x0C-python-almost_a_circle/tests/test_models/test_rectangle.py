import unittest
import pep8
import sys
from models.rectangle import Rectangle
from models.base import Base


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
    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        Base.__nb_objects = 0

    def test_id(self):
        self.assertEqual(self.r1.id, 11)
        self.assertEqual(self.r2.id, 12)
        self.assertEqual(self.r3.id, 12)

    def test_width(self):
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 10)

    def test_height(self):
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r3.height, 2)

    def test_x(self):
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r3.x, 0)

    def test_y(self):
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 0)

    def test_area(self):
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 20)
        self.assertEqual(self.r3.area(), 20)

    """
    def test_display(self):

    def test_dictionary(self):
    """

    def test_update(self):
        self.r1.update(89)
        self.assertEqual(self.r1.id, 89)

        self.r1.update(89, 2)
        self.assertEqual(self.r1.width, 2)

        self.r1.update(89, 2, 3)
        self.assertEqual(self.r1.height, 3)

        self.r1.update(89, 2, 3, 4)
        self.assertEqual(self.r1.x, 4)

        self.r2.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r2.y, 5)

    def test_update(self):
        self.r1.update(height=1)
        self.assertEqual(self.r1.height, 1)

        self.r1.update(width=1, x=2)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.x, 2)

        self.r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.x, 3)
        self.assertEqual(self.r1.id, 89)

        self.r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(self.r1.x, 1)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.y, 3)
        self.assertEqual(self.r1.width, 4)

    def test_errors(self):
        with self.assertRaises(TypeError):
            self.r3.height = "2"
            self.r2.height = "2"
            self.r1.height = "2"

        with self.assertRaises(TypeError):
            self.r3.width = "2"
            self.r2.width = "2"
            self.r1.width = "2"

        with self.assertRaises(TypeError):
            self.r3.x = "2"
            self.r2.x = "2"
            self.r1.x = "2"

        with self.assertRaises(TypeError):
            self.r3.y = "2"
            self.r2.y = "2"
            self.r1.y = "2"

        with self.assertRaises(ValueError):
            self.r3.height = -10
            self.r2.height = -10
            self.r1.height = -10

        with self.assertRaises(ValueError):
            self.r3.width = -10
            self.r2.width = -10
            self.r1.width = -10

        with self.assertRaises(ValueError):
            self.r3.x = -10
            self.r2.x = -10
            self.r1.x = -10

        with self.assertRaises(ValueError):
            self.r3.y = -10
            self.r2.y = -10
            self.r1.y = -10
