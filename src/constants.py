''' constants '''

class constants:
    """ Global file declarations """
    BUFFERSIZE   = 128
    EOS     = '\0'
    EOF     = True
    SYMBOL_TABLE = []

    COMMENTS = 255
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
        self.token = value
        self.lexeme = lex

E = {
    "null-character":
        "Null character in input stream, replaced with U+FFFD.",
    "invalid-codepoint":
        "Invalid codepoint in stream.",
}

tokenTypes = {
    "Doctype": 0,
    "Characters": 1,
    "SpaceCharacters": 2,
    "StartTag": 3,
    "EndTag": 4,
    "EmptyTag": 5,
    "Comment": 6,
    "ParseError": 7
}