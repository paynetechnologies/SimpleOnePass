from collections import namedtuple

class entry(object):
    """ a symbol table enry """

    def __init__(self, lex, value):
        self.lexptr = lex
        self.token = value

    # lexptr = ''
    # token = 0


class globals(self):

    BSIZE   = 128
    NONE    = -1
    EOS     = '\0'
    NUM     = 255
    DIV     = 257
    MOD     = 258
    ID      = 259
    DONE    = 260

    tokenval = 0
    lineno   = 0
    symboltable = []

    # namedtuple is immutable
    # entry = namedtuple("entry", "lexptr token")


if __name__ == '__main__':
    test_entry()