import sys
import error
import globals
from symbol import insert

keywords = {'div' : 'DIV', 'mod' : 'MOD'}

def init():
    '''Loads keywords into SYMBOL_TABLE'''
    globals.SYMBOL_TABLE = (insert(lex, tok) for lex,tok in keywords)