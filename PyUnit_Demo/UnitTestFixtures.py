import unittest


class UnitTestFixtures(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setup Class")

    def setUp(self):
        print("Setup test")

    def test3(self):
        print("test3")

    def test2(self):
        print("test2")

    def test1(self):
        print("test1")

    def tearDown(self):
        print("teardown test")

    @classmethod
    def tearDownClass(cls):
        print("teardown class")
if __name__ == '__main__':
    unittest.main()