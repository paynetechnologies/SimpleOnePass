import sys
import src.error
from src.constants import constants, entry
from src.symbol_table import lookup, insert

keywords = {'div' : 'DIV', 'mod' : 'MOD'}

def init_symbol_table():
    '''Loads keywords into SYMBOL_TABLE'''
    print('init_symbol_table')
    for lex,tok in keywords.items():
        insert(lex, tok) 
    #constants.SYMBOL_TABLE = (symbol_table.insert(lex, tok) for lex,tok in keywords)
    for entry in constants.SYMBOL_TABLE:
        print(f'id : {entry.lex} - token : {entry.token}') 

if (__name__ == "__main__"):
    init_symbol_table()