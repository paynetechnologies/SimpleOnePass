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


    # i = 1
    # c = ii_advance()
    # print(f'First char : {chr(c)}')
    
    # while not NO_MORE_CHARS(self):
    #     i+=1
    #     c = ii_advance()
    #     if c != -1:
    #         pass
    #         #print(f'c : {i} - {chr(c)}')
    #         #print(chr(c))
    #     elif c == -1:
    #         #print(f'Next Char : {i}')
    #         ii_mark_prev()
    #         ii_mark_start()          
    # printBuf()        
