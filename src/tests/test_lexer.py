import unittest
from src.constants import constants, entry
from src.lexer import lexer
from src.init import init

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
        init.init_symbol_table()

    @classmethod
    def tearDownClass(cls):
        init.clear_symbol_table()

    def setUp(self): 
        self.lex = lexer()
        self.assertIsNotNone(self.lex)

    def tearDown(self):
        return super().tearDown()



    def test_01_newline(self):
        self.lex.loadBuffer('\n')
        token = self.lex.tokenizer()
        self.assertEqual(constants.NEWLINE, token)

    def test_02_White_Space(self):
        # '   '
        self.lex.loadBuffer('  whitespace ')
        token = self.lex.tokenizer()
        self.assertEqual(constants.WHITESPACE, token)

    def test_03_Single_Digit(self):
        # ' 1 '
        self.lex.loadBuffer('1')
        token = self.lex.tokenizer()
        self.assertEqual(constants.NUM, token)

    def test_04_Multiple_Digits(self):
        # ' 123 '
        self.lex.loadBuffer('123')
        token = self.lex.tokenizer()
        self.assertEqual(constants.NUM, token)

    def test_05_Alpha(self):
        # 'abc  '
        self.lex.loadBuffer('abc ')
        token = self.lex.tokenizer()
        self.assertEqual(constants.ID, token)

    def test_06_Alphanumeric(self):
        #  'abc123 '
        self.lex.loadBuffer('abc1d2e ')
        token = self.lex.tokenizer()
        self.assertEqual(constants.ID, token)

    def test_07_EmptyString(self):
        # ''
        self.lex.loadBuffer(' ')
        token = self.lex.tokenizer()
        self.assertEqual(constants.WHITESPACE, token)        

    def test_08_EOF (self):
        # ''
        self.lex.loadBuffer('')
        token = self.lex.tokenizer()
        self.assertEqual(constants.DONE, token)        

    def test_09_operators(self):
        # +, -, /, *, DIV, MOD
        self.lex.loadBuffer('DIV ')
        token = self.lex.tokenizer()
        self.assertEqual(constants.DIV, token)        

    def test_10_operators(self):
        # +, -, /, *, DIV, MOD
        self.lex.loadBuffer('MOD ')
        token = self.lex.tokenizer()
        self.assertEqual(constants.MOD, token)        

if __name__ == '__main__':
    unittest.main()