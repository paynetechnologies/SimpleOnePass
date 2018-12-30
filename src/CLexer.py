import string
import sys

from src.CInput import CInput
from src.token import Token

class CLexer:

    EOF_MARKER = '$'
    WHITESPACE = ' \t\r\n'
    NEWLINE = '\n'
    COMMENT_MARKER = '#'
    HTML_COMMENT = '<!--'
    LESS_THAN = '<'
    GREATER_THAN = '>'
    DASH = '-'
    EXCLAMATION = '!'
    QUOTE = '"'
    TIC = "'"
    MAX_QT_LEN = 256
    OPERATORS = '+-*/=<>!'
    PUNCTUATORS = '.?:[](),;#\'"_@\\\/~%'


    def __init__(self, input):
        
        self.line_no = 0
        self.line_pos = 0
        self.token_value = None    
        self.tokens = [] 
        self.input = input


    def getchar(self):

        c = self.input.ii_advance(0)
        self.line_pos += 1
        return (chr(c))

    def tokenizer(self, input):

        c = self.getchar()
        while not input.NO_MORE_CHARS():

            # whitespace
            if c in CLexer.WHITESPACE:
                #while c in CLexer.WHITESPACE and not input.NO_MORE_CHARS():
                if c in CLexer.NEWLINE:
                    self.line_no += 1
                    self.line_pos = 0

                c = self.getchar()
                input.ii_mark_prev()
                input.ii_mark_start() 

            # single line comment
            elif c in CLexer.COMMENT_MARKER:
                match = c
                c = self.getchar()
                while c not in CLexer.NEWLINE and not input.NO_MORE_CHARS():
                    match += c        
                    if c in CLexer.NEWLINE:
                        self.line_no += 1
                        self.line_pos = 0                                              
                    c = self.getchar()

                input.ii_mark_prev()
                input.ii_mark_start() 

            # html comment <!-- -->
            elif c in CLexer.LESS_THAN:
                match = c
                if  (chr(input.ii_look(1)) == CLexer.EXCLAMATION) \
                    and (chr(input.ii_look(2)) == CLexer.DASH) \
                    and (chr(input.ii_look(3)) == CLexer.DASH):
                   
                    while True and not input.NO_MORE_CHARS():
                        c = self.getchar()
                        match += c                                                                
                        if c in CLexer.NEWLINE:
                            self.line_no += 1
                            self.line_pos = 0                                

                        if c in CLexer.GREATER_THAN \
                        and (chr(input.ii_look(-1)) == CLexer.DASH) \
                        and (chr(input.ii_look(-2)) == CLexer.DASH):
                            break

                    token = Token(Token.HTML_COMMENT, match, self.line_no, self.line_pos)
                    self.tokens.append(token) 

                # Less Than < sign
                else:
                    token = Token(Token.LESS_THAN, c, self.line_no, self.line_pos)
                    self.tokens.append(token)       

                c = self.getchar()
                input.ii_mark_prev()
                input.ii_mark_start()                     

            # identifier
            elif c.isalpha(): #in string.ascii_letters:
                match = c
                c = self.getchar()

                while c.isalnum() and not input.NO_MORE_CHARS(): #in string.ascii_letters:
                    match += c
                    if c in CLexer.NEWLINE:
                        self.line_no += 1
                        self.line_pos = 0                      
                    c = self.getchar()

                token = Token(Token.IDENT, match, self.line_no, self.line_pos)
                self.tokens.append(token)

                input.ii_mark_prev()
                input.ii_mark_start()                 

            # number
            elif (c in string.digits):

                match = c
                Token.token_value = int(c) - 0
                c = self.getchar()

                while(c in string.digits) and not input.NO_MORE_CHARS():                    
                    match += c
                    if c in CLexer.NEWLINE:
                        self.line_no += 1
                        self.line_pos = 0  
                    Token.token_value = Token.token_value * 10 + int(c) - 0
                    c = self.getchar()

                token = Token(Token.NUM, match, self.line_no, self.line_pos)
                self.tokens.append(token)                   
                # return Token.NUM    
        
                input.ii_mark_prev()
                input.ii_mark_start()                 

            # Greater Than > sign
            elif c in CLexer.GREATER_THAN:

                token = Token(Token.GREATER_THAN, c, self.line_no, self.line_pos)
                self.tokens.append(token)      

                c = self.getchar()
                input.ii_mark_prev()
                input.ii_mark_start()          

            # Quoted Identifier
            elif c in CLexer.QUOTE:

                match = c                                                       # begin "        
                c = self.getchar()            
                while c not in  CLexer.QUOTE and not self.input.NO_MORE_CHARS():                                           # quoted literal 
                    match += c                                
                    c = self.getchar()
                match += c                                                      # end "

                token = Token(Token.QUOTEDIDENT, match, self.line_no, self.line_pos)
                self.tokens.append(token) 

                c = self.getchar()
                input.ii_mark_prev()
                input.ii_mark_start()                    

            # operators
            elif c in CLexer.OPERATORS:

                token = Token(Token.OPERATOR, c,  self.line_no, self.line_pos)
                self.tokens.append(token)
                
                c = self.getchar()
                input.ii_mark_prev()
                input.ii_mark_start()                 

            # punctuators
            elif c in CLexer.PUNCTUATORS:

                token = Token(Token.PUNCTUATION, c, self.line_no, self.line_pos)
                self.tokens.append(token)

                c = self.getchar()
                input.ii_mark_prev()
                input.ii_mark_start()                           

            # start block
            elif c == '{':

                token = Token(Token.BEGIN_BLOCK, c, self.line_no, self.line_pos)
                self.tokens.append(token)

                c = self.getchar()
                input.ii_mark_prev()
                input.ii_mark_start()                 

            # end block
            elif c == '}':       

                token = Token(Token.END_BLOCK, c, self.line_no, self.line_pos)
                self.tokens.append(token)

                c = self.getchar()
                input.ii_mark_prev()
                input.ii_mark_start()                 

            else:
                raise ValueError('Unexpected character found: {0}:{1} -> {2}'.format(self.line_no + 1, self.line_pos + 1, c))

        # end of file token


        token = Token(Token.EOF, '$', self.line_no, self.line_pos)
        self.tokens.append(token)

        return self.tokens                

    def GetQuotedIdent(self, c):

        match = c                                                       # begin "        
        c = self.getchar()            
        while c not in  CLexer.QUOTE and not self.input.NO_MORE_CHARS():                                           # quoted literal 
            match += c                                
            c = self.getchar()
        match += c                                                      # end "

        token = Token(Token.QUOTEDIDENT, match, self.line_no, self.line_pos)
        self.tokens.append(token) 

if __name__ == '__main__':
    cinput = CInput('./src/test_files/web.config2')
    lexer = CLexer(cinput)
    token = lexer.tokenizer(cinput)

    # on EOF, print the tokens    
    # for token in lexer.tokens:
    #     print(token)