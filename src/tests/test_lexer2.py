import unittest
from src.lexer2 import Lexer
from src.error import error

#import tokenize


class Test_Lexer2(unittest.TestCase):
    """ Test lexer2 variables """

    # def test_01_lexer2(self):
    #     lexer = Lexer('a = b * 2')
    #     for token in lexer.tokenise():
    #         print (token)

    def test_02_lexer2(self):
        try:
            filename = "C:/Users/Howard David Payne/dev/compilers/SimpleOnePass/src/tests/tokenize-example-2.py"
            file = open(filename)
        except:       
            error(f'cannot open file {"tokenize-example-2.py"}')     
            exit(self, 0)
        lexer = Lexer(file.read())
        for token in lexer.tokenise():
            print (token)

if __name__ == '__main__':
    unittest.main()