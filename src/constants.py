''' constants '''

class constants:
    """ Global file declarations """
    BUFFERSIZE   = 128
    EOS     = '\0'
    EOF     = True
    SYMBOL_TABLE = []

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
    """ a symbol table entry """
    def __init__(self, lex, value):
        self.lexeme = lex
        self.token = value

