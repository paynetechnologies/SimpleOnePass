import unittest
from src.constants import constants
from src.symbol_table import entry, symbol_table

class Test_Constants(unittest.TestCase):
    """ Test global variables """
    
    def setUp(self):
        print('\nTest_Constants')
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()

    def test_01_constants(self):
        pass

if __name__ == '__main__':
    unittest.main()