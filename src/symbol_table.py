import sys
from src.error import lex_error_message, general_error_message
#from src.constants import constants, entry


class entry:
    """ a symbol table entry """
    def __init__(self, token, value):
        self.token = token
        self.lexeme = value


class symbol_table():

    SYMBOL_TABLE=[]

    SYMMAX = 100 # size of symbol table
    last_entry = -1

    # def __init__(self):
    #     super().__init__()
    #     self.last_entry = -1 # last used position in symtabl

    @classmethod
    def lookup(cls, value):
        """ Returns postion of entry for s """
        #for (p = last_entry; p > 0 ; p -= 1):
        for indx, entry in reversed(list(enumerate(symbol_table.SYMBOL_TABLE))):
            if (value == entry.lexeme):
                print (f'indx : {indx} - entry {entry.lexeme, entry.token}')
                return indx
        return None
        
    @classmethod
    def add(cls, token, value):
        symbol_table.last_entry += 1
        
        if (symbol_table.last_entry >= symbol_table.SYMMAX):
            general_error_message("Symbol Table Full")
       
        new_entry = entry(value, token)
        symbol_table.SYMBOL_TABLE.insert(symbol_table.last_entry, new_entry)
        return symbol_table.last_entry

    @classmethod
    def addEntry(cls, entry):
        symbol_table.last_entry += 1
        
        if (symbol_table.last_entry >= symbol_table.SYMMAX):
            general_error_message("Symbol Table Full")
       
        symbol_table.SYMBOL_TABLE.insert(symbol_table.last_entry, entry)
        return symbol_table.last_entry

if __name__ == '__main__':
    symbol_table.add('DIV', 'DIV')
    symbol_table.lookup('DIV')    