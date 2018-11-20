import unittest
from src.tests.test_entry import Test_Entry
from src.tests.test_constants import Test_Constants
from src.tests.test_init import Test_Init
from src.tests.test_lexer import Test_Lexer
from src.tests.test_lexer2 import Test_Lexer2
from src.tests.test_main import Test_Main
from src.tests.test_parser import Test_Parser
from src.tests.test_symbol import Test_Symbol_Table


class Test_Suite(unittest.TestCase):
    """ Suite of Test Class/Cases """

    def suite(self):
        print("WHAT")
        print('suite...')
        suite = unittest.TestSuite()
        result = unittest.TestResult()
        # suite.addTest(Test_Constants.test_01_constants(self))
        
        # suite.addTest(Test_Entry.test_01_create_entry(self))
        
        # suite.addTest(Test_Init.test_init_symbol_table(self))
        
        # suite.addTest(Test_Lexer.test_01_newline(self))
        # suite.addTest(Test_Lexer.test_02_White_Space(self))
        # suite.addTest(Test_Lexer.test_03_Single_Digit(self))
        # suite.addTest(Test_Lexer.test_04_Multiple_Digits(self))
        # suite.addTest(Test_Lexer2.test_01_lexer_can_read_a_file(self))
        # suite.addTest(Test_Main.test_01_main(self))
        # suite.addTest(Test_Parser.test_add_parse(self))
        # suite.addTest(Test_Parser.test_multiply_parse(self))
        # suite.addTest(Test_Symbol_Table.test_01_append_entry_to_symbolTable(self))                                        
        suite.addTest(Test_Symbol_Table.test_02_add_entry_to_symbolTable(self))

        runner = unittest.TextTestRunner()
        print(runner.run(suite))        
        return suite

if __name__ == '__main__':
    unittest.main()
