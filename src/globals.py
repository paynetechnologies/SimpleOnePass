
class constants:
    """ Global file declarations """
    BSIZE   = 128
    DIV     = 257
    DONE    = 260
    EOS     = '\0'
    EOF     = False
    ID      = 259
    LINE_NUMBER   = 0
    MOD     = 258
    NONE    = -1
    NUM     = 255
    SYMBOL_TABLE = []
    TOKEN_VALUE = 0

class entry:
    """ a symbol table enry """
    def __init__(self, lex, value):
        self.lex = lex
        self.token = value

