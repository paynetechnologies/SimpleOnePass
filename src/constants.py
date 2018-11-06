
class constants:
    """ Global file declarations """
    BSIZE   = 128
    DIV     = 256
    DONE    = 257
    EOS     = '\0'
    EOF     = False
    ID      = 258
    LINE_NUMBER   = 0
    MOD     = 259
    NEWLINE = 260
    NONE    = -1
    NUM     = 261
    OPERATOR = 262
    SYMBOL_TABLE = []
    TOKEN_VALUE = 0
    WHITESPACE = 999

class entry:
    """ a symbol table enry """
    def __init__(self, lex, value):
        self.lex = lex
        self.token = value

