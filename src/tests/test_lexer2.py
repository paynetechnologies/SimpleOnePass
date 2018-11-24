import sys
import os
import unittest
from src.error import lex_error_message
from src.lexer2 import Lexer



class Test_Lexer2(unittest.TestCase):
    """ Test lexer2 variables """

    def setUp(self):
        print('\n\n*** Test_Lexer2')
        
    # def test_01_lexer_can_read_a_string(self):
    #     lexer = Lexer('a = b * 2')
    #     for token in lexer.tokenise():
    #         print (token)

    def test_01_lexer_can_read_a_file(self):
        try:
            #home_filename = "H:\repos\dev\compilers\SimpleOnePass\src\tests\tokenize-example-2.py"
            #work_filename = "C:/Users/Howard David Payne/dev/compilers/SimpleOnePass/src/tests/tokenize-example-2.py"
            filename = "./tests/tokenize-example-2.py"
            filename = "tests/tokenize-example-2.py" # running from src dir with python tests/test_lexer2.py
            file = open(filename)
        except:       
            lex_error_message(1, f'cannot open file {"tokenize-example-2.py"}')     
            #sys.exit(0)
            os._exit(1)

        lexer = Lexer(file.read())
        
        for token in lexer.tokenise():
            print (token)
        
        file.close()

if __name__ == '__main__':
    unittest.main()