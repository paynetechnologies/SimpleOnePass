import unittest
from src.tests.test_entry import Test_Entry
# from src.tests.test_constants import Test_Constants
from src.tests.test_init import Test_Init
from src.tests.test_lexer import Test_Lexer
from src.tests.test_lexer2 import Test_Lexer2
from src.tests.test_main import Test_Main
from src.tests.test_parser import Test_Parser
from src.tests.test_symbol import Test_Symbol_Table


class Test_Suite(unittest.TestCase):
    """ Suite of Test Class/Cases """

    def suite(self):
        print('suite...')
        suite = unittest.TestSuite()
        result = unittest.TestResult()
        runner = unittest.TextTestRunner()
        print(runner.run(suite))        
        return suite

if __name__ == '__main__':
    unittest.main()
