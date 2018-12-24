import sys
import string

from src.parser import parser
from src.init import init
from src.CInput import CInput
from src.CLexer import CLexer
from src.token import Token

if __name__ == '__main__':
    
    input = CInput('./src/test_files/web.config2')
    lexer = CLexer(input)
    token = lexer.tokenizer(input)

    # on EOF, print the tokens    
    for token in lexer.tokens:
        print(token)