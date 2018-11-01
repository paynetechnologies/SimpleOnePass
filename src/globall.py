""" Global file declarations """
BSIZE   = 128
DIV     = 257
DONE    = 260
EOS     = '\0'
EOF     = False
ID      = 259
MOD     = 258
NONE    = -1
NUM     = 255

LINE_NUMBER   = 0
SYMBOL_TABLE = []
TOKEN_VALUE = 0

class Entry(object):
    """ a symbol table enry """

    def __init__(self, lex, value):
        self.lexptr = lex
        self.token = value

