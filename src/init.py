import sys
import src.error
from src.constants import constants, entry
from src.symbol_table import symbol_table
from src.token import Token

keywords = {'DIV' : Token.DIV, 'MOD' : Token.MOD}

class init:
    def __init__(self):
        super().__init__()

    @classmethod
    def clear_symbol_table(cls):
        constants.SYMBOL_TABLE = []
    
    @classmethod
    def init_symbol_table(cls):
        '''Loads keywords into SYMBOL_TABLE'''
        print('init_symbol_table')

        for lex,tok in keywords.items():
            symbol_table.insert(lex, tok) 

        #constants.SYMBOL_TABLE = (insert(lex, tok) for lex,tok in keywords.items())
        for entry in constants.SYMBOL_TABLE:
            print(f'lexeme : {entry.lexeme} - token : {entry.token}') 

    @classmethod
    def init_symboltable(cls):
        clear_symbol_table()
        init_symbol_table()

if (__name__ == "__main__"):
    i = init()
    init.clear_symbol_table()
    init.init_symbol_table()

