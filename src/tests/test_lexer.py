import unittest
from src.lexer import lexer
from src.init import init
from src.token import Token

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
        print('\n*** Test_Lexer')
        # init.clear_symbol_table()
        # init.init_symbol_table()

    @classmethod
    def tearDownClass(cls):
        init.clear_symbol_table()

    def setUp(self): 
        init.clear_symbol_table()
        init.init_symbol_table()        
        self.lex = lexer()
        self.assertIsNotNone(self.lex)


    def tearDown(self):
        return super().tearDown()

    def test_01_newline(self):
        print(f'\ntest_01_newline')
        self.lex.loadBuffer('\n\n\n NEWLINE')
        token = self.lex.tokenizer()
        self.assertEqual(Token.ID, token)

    def test_02_White_Space(self):
        print(f'\ntest_02_White_Space')
        # '   '
        self.lex.loadBuffer('          whitespace ')
        token = self.lex.tokenizer()
        self.assertEqual(Token.ID, token)

    def test_03_Single_Digit(self):
        print(f'\ntest_03_Single_Digit')
        # ' 1 '
        self.lex.loadBuffer(' 1 ')
        token = self.lex.tokenizer()
        self.assertEqual(Token.NUM, token)

    def test_04_Multiple_Digits(self):
        print(f'\ntest_04_Multiple_Digits')
        # ' 123 '
        self.lex.loadBuffer(' 123 ')
        token = self.lex.tokenizer()
        self.assertEqual(Token.NUM, token)

    def test_05_Alpha(self):
        print(f'\ntest_05_Alpha')
        # 'abc  '
        self.lex.loadBuffer(' abc ')
        token = self.lex.tokenizer()
        self.assertEqual(Token.ID, token)

    def test_06_Alphanumeric(self):
        print(f'\ntest_06_Alphanumeric')
        #  'abc123 '
        self.lex.loadBuffer(' abc123 ')
        token = self.lex.tokenizer()
        self.assertEqual(Token.ID, token)

    def test_07_EmptyString(self):
        print(f'\ntest_07_EmptyString')
        # ' '
        self.lex.loadBuffer(' ')
        token = self.lex.tokenizer()
        self.assertEqual(Token.EOF, token)        

    def test_08_EOF(self):
        print(f'\ntest_05_Alpha')
        # ''
        self.lex.loadBuffer('')
        token = self.lex.tokenizer()
        self.assertEqual(Token.EOF, token)        

    def test_09_DIV_operators(self):
        print(f'\ntest_09_DIV_operators')
        # DIV
        self.lex.loadBuffer(' DIV ')
        token = self.lex.tokenizer()
        self.assertEqual(Token.DIV, token)        

    def test_10_MOD_operators(self):
        print(f'\ntest_10_MOD_operators')
        # MOD
        self.lex.loadBuffer(' MOD ')
        token = self.lex.tokenizer()
        self.assertEqual(Token.MOD, token)        

    def test_11_Plus_operators(self):
        print(f'\ntest_11_Plus_operators')
        # +
        self.lex.loadBuffer(' + ')
        token = self.lex.tokenizer()
        self.assertEqual('+', token)        

    def test_12_Minus_operators(self):
        print(f'\ntest_12_Minus_operators')
        # -
        self.lex.loadBuffer(' - ')
        token = self.lex.tokenizer()
        self.assertEqual('-', token)        

    def test_13_Div_operators(self):
        print(f'\ntest_13_Div_operators')
        # /
        self.lex.loadBuffer(' / ')
        token = self.lex.tokenizer()
        self.assertEqual('/', token)        

    def test_14_Mult_operators(self):
        print(f'\ntest_14_Mult_operators')
        # *
        self.lex.loadBuffer(' * ')
        token = self.lex.tokenizer()
        self.assertEqual('*', token)        

if __name__ == '__main__':
    unittest.main()