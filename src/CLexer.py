import string
import sys

from src.CInput import CInput
from src.token import Token

class CLexer:

    EOF_MARKER = '$'
    WHITESPACE = ' \t\n\r'
    NEWLINE = '\n'
    COMMENT_MARKER = '#'
    LESS_THAN = '<'
    GREATER_THAN = '>'
    DASH = '-'
    EXCLAMATION = '!'


    def __init__(self, input):
        
        self.line_no = 0
        self.line_pos = 0
        self.token_value = None    
        self.tokens = [] 
        self.input = input


    def getchar(self):

        c = input.ii_advance(0)
        self.line_pos += 1

        if c == -1:
            c = input.ii_advance(1)
            self.line_pos += 1
            input.ii_mark_prev()
            input.ii_mark_start() 
        
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
                            while c not in CLexer.GREATER_THAN:
                                match += c                                
                                c = self.getchar()
                            #c in CLexer.GREATER_THAN:
                            match += c
                            token = Token(Token.HTML_COMMENT, match, self.line_no, self.line_pos)
                            self.tokens.append(token) 
                            c = self.getchar()

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

            else:
                print(f'UNKNOWN - {c}')            
                c = self.getchar()
                input.ii_mark_prev()
                input.ii_mark_start() 

        # end of file token


        token = Token(Token.EOF, '$', self.line_no, self.line_pos)
        self.tokens.append(token)

        return self.tokens                


if __name__ == '__main__':
    input = CInput('./src/test_files/web.config2')
    lexer = CLexer(input)
    token = lexer.tokenizer(input)

    # on EOF, print the tokens    
    for token in lexer.tokens:
        print(token)