import sys
import unittest
from src.parser import parser
from src.init import init

class Test_Parser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n\nTest_Parser')
        init.init_symbol_table()

    @classmethod
    def tearDownClass(cls):
        init.clear_symbol_table()

    def test_add_parse(self):
        init()
        p = parser( 'A + B' )
        p.parse()

    def test_multiply_parse(self):
        init()
        p = parser( 'A * B' )
        p.parse()

if __name__ == '__main__':
    unittest.main()