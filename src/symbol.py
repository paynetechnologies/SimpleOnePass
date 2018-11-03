import sys
import error
import globall as G

STRMAX = 999 # size of lexeme list
SYMMAX = 100 # size of symbol table

lexemes = ['' for i in range(STRMAX)]
last_char = -1 # last used position in lexemes

#G.SYMBOL_TABLE = [G.Entry() for i in range(STRMAX)]
last_entry = -1 # last used position in symtable

def lookup(s):
    """ Returns postion of entry for s """
    # s = []
    # p = 0

    #for (p = last_entry; p > 0 ; p -= 1):
    for indx, entry in reversed(list(enumerate(G.SYMBOL_TABLE))):
        print (f'indx : {indx} - entry {entry}')
        if (s == entry):
            return indx
        return 0
    
def insert(s, tok):
    global last_entry
    l = len(s)
    
    if (last_entry + 1 >= SYMMAX):
        error("Symbol Table Full")
    
    if (last_char + l > STRMAX ):
        error("lexeme list full")
    
    last_entry += 1
    
    entry = G.Entry(s,tok)

    G.SYMBOL_TABLE.insert(last_entry,entry)

    return last_entry

if __name__ == '__main__':
    insert('howard', 'TOK')



