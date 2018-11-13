import sys
from src.error import error_message
from src.constants import constants, entry

class symbol_table():

    SYMMAX = 100 # size of symbol table

    last_entry = -1

    # def __init__(self):
    #     super().__init__()
    #     self.last_entry = -1 # last used position in symtabl

    @classmethod
    def lookup(cls, value):
        """ Returns postion of entry for s """
        #for (p = last_entry; p > 0 ; p -= 1):
        for indx, entry in reversed(list(enumerate(constants.SYMBOL_TABLE))):
            if (value == entry.lexeme):
                print (f'indx : {indx} - entry {entry.lexeme, entry.token}')
                return indx
        return None
        
    @classmethod
    def insert(cls, value, token):
        symbol_table.last_entry += 1
        
        if (symbol_table.last_entry >= symbol_table.SYMMAX):
            error_message("Symbol Table Full")
       
        new_entry = entry(value, token)
        constants.SYMBOL_TABLE.insert(symbol_table.last_entry, new_entry)
        return symbol_table.last_entry

if __name__ == '__main__':
    # st = symbol_table()
    # st.symbol_table_insert('DIV', 'DIV')
    # st.symbol_table_lookup('DIV')

    symbol_table.insert('DIV', 'DIV')
    symbol_table.lookup('DIV')    