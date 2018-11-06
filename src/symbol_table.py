import sys
import src.error
from src.constants import constants, entry

STRMAX = 999 # size of lexeme list
SYMMAX = 100 # size of symbol table

lexemes = ['' for i in range(STRMAX)]
last_char = -1 # last used position in lexemes

#constants.SYMBOL_TABLE = [constants.Entry() for i in range(STRMAX)]
last_entry = -1 # last used position in symtable

def lookup(s):
    """ Returns postion of entry for s """
    # s = []
    # p = 0

    #for (p = last_entry; p > 0 ; p -= 1):
    for indx, entry in reversed(list(enumerate(constants.SYMBOL_TABLE))):
        if (s == entry.token):
            print (f'indx : {indx} - entry {entry.lex, entry.token}')
            return indx
    return None
    
def insert(s, tok):
    global last_entry
    l = len(s)
    
    if (last_entry + 1 >= SYMMAX):
        error("Symbol Table Full")
    
    if (last_char + l > STRMAX ):
        error("lexeme list full")
    
    last_entry += 1
    
    new_entry = entry(s,tok)

    constants.SYMBOL_TABLE.insert(last_entry, new_entry)

    return last_entry

if __name__ == '__main__':
    insert('howard', 'TOK')



