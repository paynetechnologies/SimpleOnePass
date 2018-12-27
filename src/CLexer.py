import string
import sys

from src.CInput import CInput
from src.token import Token

class CLexer:

    EOF_MARKER = '$'
    WHITESPACE = ' \t\r\n'
    NEWLINE = '\n'
    COMMENT_MARKER = '#'
    LESS_THAN = '<'
    GREATER_THAN = '>'
    DASH = '-'
    EXCLAMATION = '!'
    QUOTE = '"'
    TIC = "'"


    def __init__(self, input):
        
        self.line_no = 0
        self.line_pos = 0
        self.token_value = None    
        self.tokens = [] 
        self.input = input


    def getchar(self):

        c = self.input.ii_advance(0)
        self.line_pos += 1

        if c == -1:
            c = self.input.ii_advance(1)
            self.line_pos += 1
            self.input.ii_mark_prev()
            self.input.ii_mark_start() 
        
        return (chr(c))


    def tokenizer(self, input):

        c = self.getchar()
        while not input.NO_MORE_CHARS():

            # ignore whitespace
            if c in CLexer.WHITESPACE:
                if c in CLexer.NEWLINE:
                    self.line_no += 1
                    self.line_pos = 0

                c = self.getchar()

            # comment
            elif c in CLexer.COMMENT_MARKER:

                match = c
                c = self.getchar()
                while c not in CLexer.NEWLINE:
                    match += c                                
                    c = self.getchar()

                input.ii_mark_prev()
                input.ii_mark_start() 

            # html comment <!-- -->

            elif c in CLexer.LESS_THAN:
                match = c

                if (chr(input.ii_look(1)) == CLexer.EXCLAMATION):
                    if (chr(input.ii_look(2)) == CLexer.DASH):
                        if (chr(input.ii_look(3)) == CLexer.DASH):
                            c = self.getchar()
                            while c not in CLexer.GREATER_THAN:     # get comment
                                match += c                                
                                c = self.getchar()
                            match += c                              # c is >
                            token = Token(Token.HTML_COMMENT, match, self.line_no, self.line_pos)
                            self.tokens.append(token) 

                else:
                    token = Token(Token.LESS_THAN, c, self.line_no, self.line_pos)
                    self.tokens.append(token)       

                c = self.getchar()
                input.ii_mark_prev()
                input.ii_mark_start()                     

            # identifier token
            elif c.isalpha(): #in string.ascii_letters:

                match = c
                c = self.getchar()

                while c.isalnum(): #in string.ascii_letters:
                    match += c
                    c = self.getchar()

                token = Token(Token.IDENT, match, self.line_no, self.line_pos)
                self.tokens.append(token)
                # c = self.getchar()
                input.ii_mark_prev()
                input.ii_mark_start()                 

            # number
            elif (c in string.digits):

                match = c
                Token.token_value = int(c) - 0
                c = self.getchar()

                while(c in string.digits):                    
                    match += c
                    Token.token_value = Token.token_value * 10 + int(c) - 0
                    c = self.getchar()

                token = Token(Token.NUM, match, self.line_no, self.line_pos)
                self.tokens.append(token)                   
                # return Token.NUM    
        
                input.ii_mark_prev()
                input.ii_mark_start()                 

            elif c in CLexer.GREATER_THAN:

                token = Token(Token.GREATER_THAN, c, self.line_no, self.line_pos)
                self.tokens.append(token)      

                c = self.getchar()
                input.ii_mark_prev()
                input.ii_mark_start()          

            # operators
            elif c in '+-*/=<>!':

                token = Token(Token.OPERATOR, c,  self.line_no, self.line_pos)
                self.tokens.append(token)
                
                c = self.getchar()
                input.ii_mark_prev()
                input.ii_mark_start()                 

            # Quoted Identifier
            elif c in '"':

                self.GetQuotedIdent(c)
                c = self.getchar()
                
                input.ii_mark_prev()
                input.ii_mark_start()                    

            # punctuators
            elif c in '.?:[](),;#"_@\/~%':

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
                c = self.getchar()
                input.ii_mark_prev()
                input.ii_mark_start() 

        # end of file token


        token = Token(Token.EOF, '$', self.line_no, self.line_pos)
        self.tokens.append(token)

        return self.tokens                

    def GetQuotedIdent(self, c):
        #token = Token(Token.PUNCTUATION, c, self.line_no, self.line_pos) # =
        #self.tokens.append(token)

        match = c                                                       # begin "        
        c = self.getchar()            
        while c not in ['"']:                                           # quoted literal 
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
    for token in lexer.tokens:
        print(token)

'''
        if match in token.quoted_identifiers:
            token = Token(Token.QUOTEDIDENTKEYWORD, match, self.line_no, self.line_pos)
            self.tokens.append(token)

            #self.GetQuotedIdent(c)
            if (c != "="):
                print(f'Expected =')
                continue;

            token = Token(Token.PUNCTUATION, c, self.line_no, self.line_pos)
            self.tokens.append(token)

            c = self.getchar()            
            match = c            
            self.input.ii_mark_prev()
            self.input.ii_mark_start()                 
            
            c = self.getchar()            
            while c not in ['"']:     # get quoted literal 
                match += c                                
                c = self.getchar()
            match += c                              # c is >
            token = Token(Token.QUOTEDIDENT, match, self.line_no, self.line_pos)
            self.tokens.append(token) 
            c = self.getchar()
            self.input.ii_mark_prev()
            self.input.ii_mark_start()                
'''