import sys
import src.error
from src.symbol_table import SymbolTable, Entry
from src.token import Token

keywords = {Token.DIV : 'DIV' , Token.MOD : 'MOD'}

class init:
    def __init__(self):
        super().__init__()

    @classmethod
    def clear_symbol_table(cls):
        print('\nclear_symbol_table')
        SymbolTable.symbol_table = []
    
    @classmethod
    def init_symbol_table(cls):
        '''Loads keywords into symbol_table'''
        print('init_symbol_table')

        for tok, lex in keywords.items():
            SymbolTable.add(tok, lex) 

        #constants.symbol_table = (insert(lex, tok) for lex,tok in keywords.items())
        print(f'Symbol Table Contents')
        for Entry in SymbolTable.symbol_table:
            print(f'Token : {Entry.token} -> Lexeme : {Entry.lexeme}') 

if (__name__ == "__main__"):
    i = init()
    init.clear_symbol_table()
    init.init_symbol_table()

