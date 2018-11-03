import sys
import error
import globall as G
from symbol import insert

keywords = {'div' : 'DIV', 'mod' : 'MOD'}

def init():
    '''Loads keywords into SYMBOL_TABLE'''
    G.SYMBOL_TABLE = (insert(lex, tok) for lex,tok in keywords)