import unittest

def add(a,b):
    return a+b


class SampleTest(unittest.TestCase):

    def testCalc(self):
        print(add(5,5))
        
if __name__ == '__main__':
    unittest.main()