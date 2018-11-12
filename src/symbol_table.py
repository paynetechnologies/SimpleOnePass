import sys
from src.error import error_message
from src.constants import constants, entry

class symbol_table():

    SYMMAX = 100 # size of symbol table

    def __init__(self):
        super().__init__()
        self.last_entry = -1 # last used position in symtabl

    def st_lookup(self, value):
        """ Returns postion of entry for s """
        #for (p = last_entry; p > 0 ; p -= 1):
        for indx, entry in reversed(list(enumerate(constants.SYMBOL_TABLE))):
            if (value == entry.lexeme):
                print (f'indx : {indx} - entry {entry.lexeme, entry.token}')
                return indx
        return None
        
    def st_insert(self, value, token):
        self.last_entry += 1
        
        if (self.last_entry >= symbol_table.SYMMAX):
            error_message("Symbol Table Full")
       
        new_entry = entry(value, token)
        constants.SYMBOL_TABLE.insert(self.last_entry, new_entry)

if __name__ == '__main__':
    st = symbol_table()
    st.st_insert('DIV', 'DIV')
    st.st_lookup('DIV')