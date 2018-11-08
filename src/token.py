

class Token(object):
    eof = 'END-OF-FILE'
    ident = 'IDENT'
    number = 'NUMBER'
    operator = 'OP'

    DIV     = 256
    DONE    = 257
    ID      = 258
    MOD     = 259
    NEWLINE = 260
    NONE    = -1
    NUM     = 261
    OPERATOR = 262
    WHITESPACE = 999    

    def __init__(self, type, value, line, line_no, line_pos):
        self.type = type
        self.value = value
        self.line = line
        self.line_pos = line_pos - len(value)
        self.line_no = line_no

    def __str__(self):
        return '{0}:{1}'.format(self.line_no + 1, self.line_pos).ljust(10) + self.type.ljust(15) + self.value