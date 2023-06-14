import unittest

class skipTestEg(unittest.TestCase):
    @unittest.skip("Skipping test3")
    def test3(self):
        print("test3")

    @unittest.skipIf(1==1,"Skipping if my condition s true")
    def test2(self):
        print("test2")

    @unittest.skipUnless(1 == 10, "Skipping if my condition s false")
    def test1(self):
        print("test1")

    def test4(self):
        print("Hello test4")
        self.skipTest("Skipping after execution")
        print("test4")

    @unittest.expectedFailure
    def test5(self):
        self.assertTrue(True)
if __name__ == '__main__':
    unittest.main()