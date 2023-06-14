import unittest

class Assertion(unittest.TestCase):
    def test1(self):
        self.assertEqual(2+2,40,"Checking 2+2 is 4")

if __name__ == '__main__':
    unittest.main()

