""" Global file declarations """

class Entry(object):
    """ a symbol table enry """

    def __init__(self, lex, value):
        self.lexptr = lex
        self.token = value



# class Globals(object):
#     """global delcarations """

BSIZE   = 128
NONE    = -1
EOS     = '\0'
NUM     = 255
DIV     = 257
MOD     = 258
ID      = 259
DONE    = 260

token_value = 0
line_nbr   = 0
symbol_table = []
