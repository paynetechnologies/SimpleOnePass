import sys
import src.error
from src.symbol_table import symbol_table, entry
from src.token import Token

keywords = {'DIV' : Token.DIV, 'MOD' : Token.MOD}

class init:
    def __init__(self):
        super().__init__()

    @classmethod
    def clear_symbol_table(cls):
        symbol_table.SYMBOL_TABLE = []
    
    @classmethod
    def init_symbol_table(cls):
        '''Loads keywords into SYMBOL_TABLE'''
        print('init_symbol_table')

        for lex,tok in keywords.items():
            symbol_table.insert(lex, tok) 

        #constants.SYMBOL_TABLE = (insert(lex, tok) for lex,tok in keywords.items())
        for entry in symbol_table.SYMBOL_TABLE:
            print(f'Token : {entry.token} -> Lexeme : {entry.lexeme}') 

    @classmethod
    def init_symboltable(cls):
        init.clear_symbol_table()
        init.init_symbol_table()

if (__name__ == "__main__"):
    i = init()
    init.clear_symbol_table()
    init.init_symbol_table()

