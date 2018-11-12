import sys
import src.error
from src.constants import constants, entry
from src.symbol_table import symbol_table

keywords = {'DIV' : constants.DIV, 'MOD' : constants.MOD}

   
def clear_symbol_table():
    constants.SYMBOL_TABLE = []

def init_symbol_table(st):
    '''Loads keywords into SYMBOL_TABLE'''
    print('init_symbol_table')

    for lex,tok in keywords.items():
        st.insert(lex, tok) 

    #constants.SYMBOL_TABLE = (insert(lex, tok) for lex,tok in keywords.items())
    for entry in constants.SYMBOL_TABLE:
        print(f'lexeme : {entry.lexeme} - token : {entry.token}') 

def init():
    st = symbol_table()
    clear_symbol_table()
    init_symbol_table(st)

if (__name__ == "__main__"):
    init()