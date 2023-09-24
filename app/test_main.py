from main import home, reverse_string
import unittest

class TestMain(unittest.TestCase):
    def test_home(self):
        self.assertEquals("Welcome!", home())

    def test_reverse_string(self):
        self.assertEquals("gnirts tset", reverse_string("test string"))

if __name__ == "__main__":
    unittest.main()