import sys
from src.error import lex_error_message, general_error_message


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
        print(f'\nSymbol Table Lookup :: value {value}')
        for indx, entry in reversed(list(enumerate(symbol_table.SYMBOL_TABLE))):
            if (value == entry.lexeme):
                print(f'index :: {indx} : value :: {value} : entry.lexeme :: {entry.lexeme}')
                return indx
        print(f'Symbol Table Lookup :: Not Found')                
        return None
        
    @classmethod
    def insert(cls, token, value):
        symbol_table.last_entry += 1
        
        if (symbol_table.last_entry >= symbol_table.SYMMAX):
            general_error_message("Symbol Table Full")
       
        new_entry = entry(token, value)
        
        symbol_table.SYMBOL_TABLE.insert(symbol_table.last_entry, new_entry)
        print(f'Symbol Table Insert :: Index = {symbol_table.last_entry} : Token = {token} : Value = {value}')
        # print(f'symbol_table_index :: {symbol_table.last_entry}')
        # print(f'symbol_table_token :: {symbol_table.SYMBOL_TABLE[symbol_table.last_entry].token}')
        # print(f'symbol_table_lexeme:: {symbol_table.SYMBOL_TABLE[symbol_table.last_entry].lexeme}')

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