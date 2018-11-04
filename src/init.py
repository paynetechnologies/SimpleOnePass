import sys
import error
from src.globals import constants, entry
from symbol import insert

keywords = {'div' : 'DIV', 'mod' : 'MOD'}

def init():
    '''Loads keywords into SYMBOL_TABLE'''
    constants.SYMBOL_TABLE = (insert(lex, tok) for lex,tok in keywords)