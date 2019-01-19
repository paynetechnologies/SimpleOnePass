'''Token Types'''
# configuration -> configurations appsettings connectionstrings system.web system.webserver 

class Token(object):

    APPSETTING          = 'APPSETTING' 
    BEGIN_BLOCK         = 'BEGIN' 
    COMMENT             = 'COMMENT'
    CONFIGURATION       = 'CONFIGURATION'
    CONFIGURATIONS      = 'CONFIGSECTIONS'
    CONNECTIONSTRINGS   = 'CONNECTIONSTRINGS'
    DASH                = 'DASH'
    DIV                 = 'DIV'
    DIVIDE              = 'DIV_OP'
    DONE                = 'DONE'
    END_BLOCK           = 'END_BLK' 
    END_NODE            = 'END_NODE' 
    END_TAG             = 'END_TAG' 
    EOF                 = 'EOF'
    EXCLAMATION         = 'EXCLAMATION'
    GREATER_THAN        = 'GT'
    HTML_COMMENT        = 'COMMENT'
    ID                  = 'ID'
    KEYWORD             = 'KW'
    LESS_THAN           = 'LT'
    MINUS               = 'MINUS_OP'
    MOD                 = 'MOD_OP'
    MULTIPLY            = 'MULT_OP'
    NAME                = 'NAME'
    NEWLINE             = 'NL'
    NONE                = 'NONE'
    NUM                 = 'NUM'
    OPERATOR            = 'OP'
    PLUS                = 'PLUS_OP'
    PUNCTUATION         = 'PCT'
    QUOTE               = 'QT'
    REL_OP              = 'RO'
    SECTION             = 'SECTION'
    START_TAG           = 'START_TAG' 
    SYSTEM_SERVICEMODEL = 'SYSTEM_SERVICEMODEL'
    SYSTEM_WEB          = 'SYSTEM_WEB'
    SYSTEM_WEBSERVER    = 'SYSTEM_WEBSERVER'
    TYPE                = 'TYPE'
    WHITESPACE          = 'WS'

    '''
    valid_tokens =  (
        'BEGIN',        'DIV',          'DONE',     'END',          'EOF',
        'ID',           'KW',           'MOD',      'NL',           'NONE',
        'NUMBER',       'PLUS',         'MINUS',    'MULTIPLY',     'TIMES',
        'DIVIDE',       'LPAREN',       'RPAREN',   'OPERATOR',     'PUNCTUATION',
        'WHITESPACE',   'REL_OP',       'QUOTE',    'LESS_THAN',    'GREATER_THAN',
        'EQUAL',        'NOT_EQUAL',    'DASH',     'EXCLAMATION',  'START_TAG',
        'END_TAG',      'QID'           'COMMENT'
    )

    tokens =  [
        'BEGIN',        'DIV',          'DONE',     'END',          'EOF',
        'ID',           'KW',           'MOD',      'NL',           'NONE',
        'NUMBER',       'PLUS',         'MINUS',    'MULTIPLY',     'TIMES',
        'DIVIDE',       'LPAREN',       'RPAREN',   'OPERATOR',     'PUNCTUATION',
        'WHITESPACE',   'REL_OP',       'QUOTE',    'LESS_THAN',    'GREATER_THAN',
        'EQUAL',        'NOT_EQUAL',    'DASH',     'EXCLAMATION',  'START_TAG',
        'END_TAG',      'QID'           'COMMENT'
    ]

    t = {
        # List of token names.   This is always required
        'BEGIN_BLOCK' : 'BEGIN',
        'DIV'         : 'DIV',
        'DONE'        : 'DONE',
        'END_BLOCK'   : 'END',  
        'EOF'         : 'EOF',
        'ID'          : 'ID',
        'IDENT'       : 'ID',
        'KEYWORD'     : 'KW',
        'MOD'         : 'MOD',
        'NEWLINE'     : 'NL',
        'NONE'        : 'NONE',
        'NUM'         : 'NUM',
        'OPERATOR'    : 'OP',
        'PUNCTUATION' : 'PCT',
        'START_TAG'   : 'ST',
        'WHITESPACE'  : 'WS',
        'PLUS'        : 'PLUS_OP',
        'MINUS'       : 'MINUS_OP',
        'MULTIPLY'    : 'MULT_OP',
        'DIVIDE'      : 'DIV_OP',
        'QUOTE'       : 'QT',
        'LESS_THAN'       : 'LT',
        'GREATER_THAN'    : 'GT',
        'DASH'            : 'DASH',
        'EXCLAMATION'     : 'EXCLAMATION',
        'APPSETTING'          : 'APPSETTING',
        'CONFIGURATION'       : 'CONFIGURATION',
        'CONFIGURATIONS'      : 'CONFIGSECTIONS',
        'CONNECTIONSTRINGS'   : 'CONNECTIONSTRINGS',
        'HTML_COMMENT'        : 'COMMENT',
        'NAME'                : 'NAME',
        'SECTION'             : 'SECTION',
        'SYSTEM_WEB'          : 'SYSTEM_WEB',
        'SYSTEM_WEBSERVER'    : 'SYSTEM_WEBSERVER',
        'SYSTEM_SERVICEMODEL' : 'SYSTEM_SERVICEMODEL',
        'TYPE'                : 'TYPE'
    }
    '''
    quoted_identifiers = ['name', 'type', 'key', 'value']
    QUOTEDIDENTKEYWORD = "QIDKEYWORD"
    QUOTEDIDENT = "QID"


    keywords    = ['if', 'else', 'elif', 'while']

    keyword_tokens = (
        'if', 'else', 'elif', 'while'
    )
   
        
    # config_tokens = (        
    #     'APPSETTING',           'CONFIGURATION',        'CONFIGURATIONS',
    #     'CONNECTIONSTRINGS',    'HTML_COMMENT',         'NAME',
    #     'SECTION',              'SYSTEM_WEB',           'SYSTEM_WEBSERVER',
    #     'SYSTEM_SERVICEMODEL',  'TYPE'
    # )

    # config_keywords   = (
    #     'configuration',        'configSections',   'appSettings',
    #     'connectionStrings',    'system.web',       'system.webServer', 
    #     'system.serviceModel',  'name',             'type', 
    #     'key',                  'value'
    # )

    token_value = 0


    # # Regular expression rules for simple tokens
    # t_PLUS    = r'\+'
    # t_MINUS   = r'-'
    # t_TIMES   = r'\*'
    # t_DIVIDE  = r'/'
    # t_LPAREN  = r'\('
    # t_RPAREN  = r'\)'    



    #def __init__(self, type, value, line, line_no, line_pos):
    def __init__(self, type, value, line_no, line_pos):        
        self.type = type
        self.value = value
        #self.line = line
        self.line_no = line_no
        self.line_pos = line_pos # - len(value)
        
    def __str__(self):
        #recent change
        #return '{0}:{1}'.format(self.line_no + 1, self.line_pos).ljust(10) + self.type.ljust(15) + self.value
        #return '{0}:{1}'.format(self.line_no, self.line_pos).ljust(10) + self.type.ljust(15) + self.value
        return '{0}:{1}'.format(self.line_no, self.line_pos).ljust(10) + self.type.ljust(15) + self.value        

    # A regular expression rule with some action code
    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t        