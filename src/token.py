'''Token Types'''
# configuration -> configurations appsettings connectionstrings system.web system.webserver 

class Token(object):
    
    BEGIN_BLOCK = 'BEGIN'    
    DIV         = 'DIV'
    DONE        = 'DONE'
    END_BLOCK   = 'END'    
    EOF         = 'EOF'
    ID          = 'ID'
    IDENT       = 'IDENT'
    KEYWORD     = 'KEYWORD'
    MOD         = 'MOD'
    NEWLINE     = 'NL'
    NONE        = 'NONE'
    NUM         = 'NUM'
    OPERATOR    = 'OP'
    PUNCTUATION = 'PUNC'
    WHITESPACE  = 'WS'
    PLUS        = 'PLUS_OP'
    MINUS       = 'MINUS_OP'
    MULTIPLY    = 'MULTIPLY_OP'
    DIVIDE      = 'DIVIDE_OP'
    
    CONFIGURATION   = 'CONFIGURATION'
    CONFIGURATIONS  = 'CONFIGURATIONS'
    SECTION         = 'SECTION'
    TYPE            = 'TYPE'
    APPSETTING      = 'APPSETTING'
    
    keywords    = ['if', 'else', 'elif', 'while']   
    token_value = 0
  

    def __init__(self, type, value, line, line_no, line_pos):
        self.type = type
        self.value = value
        self.line = line
        self.line_pos = line_pos - len(value)
        self.line_no = line_no

    def __str__(self):
        return '{0}:{1}'.format(self.line_no + 1, self.line_pos).ljust(10) + self.type.ljust(15) + self.value