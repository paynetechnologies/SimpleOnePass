import sys
from src.error import lex_error_message, general_error_message


class Entry:
    """ a symbol table Entry """
    def __init__(self, token, value):
        self.token = token
        self.lexeme = value


class SymbolTable():

    symbol_table=[]
    SYMMAX = 100 # size of symbol table
    last_entry = -1

    # def __init__(self):
    #     super().__init__()
    #     self.last_entry = -1 # last used position in symtabl

    @classmethod
    def lookup(cls, value):
        """ Returns postion of Entry for value """

        print(f'\nSymbolTable::lookup : Lexeme {value}')
        
        for indx, entry in reversed(list(enumerate(SymbolTable.symbol_table))):
            if (value == entry.lexeme):
                print(f'SymbolTable::Index = {indx} : Token = {entry.token} : Lexeme = {entry.lexeme}')
                return indx
        
        print(f'SymbolTable::lookup : Not Found')                
        return None
        
    
    @classmethod
    def add_entry(cls, entry):
        '''add new symbol table entry; return index of new entry'''
        
        print(f'\nSymbolTable::add_entry : Token = {entry.token} : Lexeme = {entry.lexeme}')
        
        # By inference, if we are here, then we already did a lookup and determined
        # that the lexeme did not exist and thus we add the lexeme
        # idx = cls.lookup(entry.lexeme)
        # if idx is not None:
        #     return idx

        SymbolTable.last_entry += 1
        
        if (SymbolTable.last_entry >= SymbolTable.SYMMAX):
            general_error_message("Symbol Table Full")
       
        SymbolTable.symbol_table.insert(SymbolTable.last_entry, entry)
        print(f'SymbolTable::Index = {SymbolTable.last_entry} : Token = {entry.token} : Lexeme = {entry.lexeme}')

        return SymbolTable.last_entry

    @classmethod
    def add(cls, token, value):

        new_entry = Entry(token, value)

        return (cls.add_entry(new_entry))

if __name__ == '__main__':
    SymbolTable.add('DIV', 'DIV')
    SymbolTable.add_entry(Entry('MUL','MUL'))
    SymbolTable.lookup('DIV')    
    SymbolTable.lookup('MUL')    