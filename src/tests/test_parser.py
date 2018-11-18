import sys
import unittest
from src.parser import parser
from src.init import init

class Test_Parser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    def tearDown(self):
        return super().tearDown()


    def test_simple_parse(self):
        init()
        p = parser( 'A + B' )
        p.parse()

    def test_multiply_parse(self):
        init()
        p = parser( 'A * B' )
        p.parse()

if __name__ == '__main__':
    unittest.main()