import sys
import src.error
from src.constants import constants, entry
from src.symbol_table import lookup, insert

keywords = {'DIV' : constants.DIV, 'MOD' : constants.MOD}

   
def clear_symbol_table():
    constants.SYMBOL_TABLE = []

def init_symbol_table():
    '''Loads keywords into SYMBOL_TABLE'''
    print('init_symbol_table')

    for lex,tok in keywords.items():
        insert(lex, tok) 

    #constants.SYMBOL_TABLE = (insert(lex, tok) for lex,tok in keywords.items())
    for entry in constants.SYMBOL_TABLE:
        print(f'id : {entry.lexeme} - token : {entry.token}') 

def initialize():
    clear_symbol_table()
    init_symbol_table()

if (__name__ == "__main__"):
    initialize()