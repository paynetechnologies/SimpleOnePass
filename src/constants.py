
class constants:
    """ Global file declarations """
    BSIZE   = 128
    EOS     = '\0'
    EOF     = False
    LINE_NUMBER   = 0
    SYMBOL_TABLE = []
    TOKEN_VALUE = 0

    DIV     = 256
    DONE    = 257
    ID      = 258
    MOD     = 259
    NEWLINE = 260
    NONE    = -1
    NUM     = 261
    OPERATOR = 262
    WHITESPACE = 999

class entry:
    """ a symbol table enry """
    def __init__(self, lex, value):
        self.lexeme = lex
        self.token = value

