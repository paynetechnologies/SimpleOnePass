import unittest
from src.constants import constants, entry
from src.lexer import lex_manager
from src.init import init_symbol_table, clear_symbol_table

'''
Newline
White Space
Single Digit
Multiple Digits
Alpha
Alphanumeric
Empty string
EOF ;
+, -, /, *
'''

class Test_Lexer(unittest.TestCase):
    """ Test lexer variables """
    
    @classmethod
    def setUpClass(cls):
        init_symbol_table()

    @classmethod
    def tearDownClass(cls):
        clear_symbol_table()

    def setUp(self):
        #init_symbol_table()
        self.lex = lex_manager()
        self.assertIsNotNone(self.lex)

    # def tearDown(self):
    #     return super().tearDown()

    # def test_00_setup_lex_manager(self):
    #     self.lex = lex_manager()
    #     self.assertIsNotNone(self.lex)

    def test_01_newline(self):
        self.lex.loadBuffer('\n;')
        token = self.lex.lex_analysis()
        #self.assertEqual(constants.NEWLINE, token)
        self.assertEqual(constants.DONE, token)

    def test_02_White_Space(self):
        # '   abc ;'
        self.lex.loadBuffer(' ;')
        token = self.lex.lex_analysis()
        #self.assertEqual(constants.WHITESPACE, token)
        self.assertEqual(constants.DONE, token)

    def test_03_Single_Digit(self):
        # ' 1 ;'
        self.lex.loadBuffer('1 ;')
        token = self.lex.lex_analysis()
        self.assertEqual(constants.NUM, token)

    def test_04_Multiple_Digits(self):
        # ' 123 ;'
        self.lex.loadBuffer('123 ;')
        token = self.lex.lex_analysis()
        self.assertEqual(constants.NUM, token)

    def test_05_Alpha(self):
        # 'abc  ;'
        self.lex.loadBuffer('abc ;')
        token = self.lex.lex_analysis()
        self.assertEqual(constants.ID, token)

    def test_06_Alphanumeric(self):
        #  'abc123 ;'
        self.lex.loadBuffer('abc1d2e ;')
        token = self.lex.lex_analysis()
        self.assertEqual(constants.ID, token)

    def test_07_EmptyString(self):
        # ';'
        self.lex.loadBuffer(';')
        token = self.lex.lex_analysis()
        self.assertEqual(constants.DONE, token)        


    def test_08_EOF (self):
        # ';'
        self.lex.loadBuffer(';')
        token = self.lex.lex_analysis()
        self.assertEqual(constants.DONE, token)        


    def test_09_operators(self):
        # +, -, /, *, DIV, MOD
        self.lex.loadBuffer('DIV ;')
        token = self.lex.lex_analysis()
        self.assertEqual(constants.DIV, token)        


if __name__ == '__main__':
    unittest.main()