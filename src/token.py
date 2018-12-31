'''Token Types'''
# configuration -> configurations appsettings connectionstrings system.web system.webserver 

class Token(object):
    
    BEGIN_BLOCK = 'BEGIN'    
    DIV         = 'DIV'
    DONE        = 'DONE'
    END_BLOCK   = 'END'    
    EOF         = 'EOF'
    ID          = 'ID'
    IDENT       = 'ID'
    KEYWORD     = 'KW'
    MOD         = 'MOD'
    NEWLINE     = 'NL'
    NONE        = 'NONE'
    NUM         = 'NUM'
    OPERATOR    = 'OP'
    PUNCTUATION = 'PCT'
    WHITESPACE  = 'WS'
    PLUS        = 'PLUS_OP'
    MINUS       = 'MINUS_OP'
    MULTIPLY    = 'MULT_OP'
    DIVIDE      = 'DIV_OP'
    QUOTE       = 'QT'

    LESS_THAN       = 'LT'
    GREATER_THAN    = 'GT'
    DASH            = 'DASH'
    EXCLAMATION     = 'EXCLAMATION'
    
    APPSETTING          = 'APPSETTING'    
    CONFIGURATION       = 'CONFIGURATION'
    CONFIGURATIONS      = 'CONFIGSECTIONS'
    CONNECTIONSTRINGS   = 'CONNECTIONSTRINGS'
    HTML_COMMENT        = 'COMMENT'
    Name                = 'NAME'
    SECTION             = 'SECTION'
    SYSTEM_WEB          = 'SYSTEM_WEB'
    SYSTEM_WEBSERVER    = 'SYSTEM_WEBSERVER'
    SYSTEM_SERVICEMODEL = 'SYSTEM_SERVICEMODEL'
    TYPE                = 'TYPE'

    keywords    = ['if', 'else', 'elif', 'while']

    quoted_identifiers = ['name', 'type', 'key', 'value']
    QUOTEDIDENTKEYWORD = "QIDKEYWORD"
    QUOTEDIDENT = "QID"

    config_keywords   = ['configuration', 'configSections', 'appSettings',
    'connectionStrings', 'system.web', 'system.webServer', 'system.serviceModel']

    token_value = 0
  

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
        return '{0}:{1}'.format(self.line_no, self.line_pos).ljust(10) + self.type.ljust(15) + self.value
