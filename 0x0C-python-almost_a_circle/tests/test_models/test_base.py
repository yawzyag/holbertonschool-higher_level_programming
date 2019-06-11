import unittest
import pep8
from models.base import Base


def fib(n):
    return 1 if n <= 2 else fib(n - 1) + fib(n - 2)


def setUpModule():
        print("setup module")


def tearDownModule():
        print("teardown module")


class TestStringMethods(unittest.TestCase):
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/base.py"
        file2 = "tests/test_models/test_base.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestBaseClass(unittest.TestCase):
    """
    Setupclass

    #Test id

    #Test json
    """
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

    def tearDown(self):
        self.__nb_objects = None

    def test_id(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)


class TestFib(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.n = 10

    def tearDown(self):
        print("tearDown")
        del self.n

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test_fib_assert_equal(self):
        self.assertEqual(fib(self.n), 55)

    def test_fib_assert_true(self):
        self.assertTrue(fib(self.n) == 55)

if __name__ == '__main__':
    unittest.main()
