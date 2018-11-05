import unittest
from constants import constants, entry
from lexer import lex_manager

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

    def setUp(self):
        self.lex = lex_manager()
        self.assertIsNotNone(self.lex)

    def tearDown(self):
        return super().tearDown()

    def test_01_newline(self):
        '''\n 
        abcd
        ;
        '''
        self.lex.loadBuffer('''\n 
        abcd
        ;
        ''')
        token = self.lex.lex_analysis()
        self.assertEqual(constants.NEWLINE, token)

    def test_02_White_Space(self):
        # '   abc ;'
        self.lex.loadBuffer('   abc ;')
        token = self.lex.lex_analysis()
        self.assertEqual(constants.WHITESPACE, token)

    def test_03_Single_Digit(self):
        # ' 1 ;'
        self.lex.loadBuffer(' 1 ;')
        token = self.lex.lex_analysis()

    def test_04_Multiple_Digits(self):
        # ' 123 ;'
        self.lex.loadBuffer(' 123 ;')
        token = self.lex.lex_analysis()


    def test_05_Alpha(self):
        # '  abc  ;'
        self.lex.loadBuffer(' abc ;')
        token = self.lex.lex_analysis()


    def test_06_Alphanumeric(self):
        #  ' abc123 ;'
        self.lex.loadBuffer(' abc1d2e3f ;')
        token = self.lex.lex_analysis()


    def test_07_EmptyString(self):
        # ';'
        self.lex.loadBuffer(';')
        token = self.lex.lex_analysis()


    def test_08_EOF (self):
        # ';'
        self.lex.loadBuffer(';')
        token = self.lex.lex_analysis()


    def test_09_operators(self):
        # +, -, /, *, DIV, MOD
        self.lex.loadBuffer(' DIV ;')
        token = self.lex.lex_analysis()


if __name__ == '__main__':
    unittest.main()