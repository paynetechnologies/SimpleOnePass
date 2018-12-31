import sys
import string

from src.CInput import CInput
from src.CLexer import CLexer
from src.token import Token

if __name__ == '__main__':
    
    cinput = CInput('./src/test_files/web.config2')
    lexer = CLexer(cinput)
    token = lexer.tokenizer(cinput)

    # on EOF, print the tokens    
    for token in lexer.tokens:
        print(token)