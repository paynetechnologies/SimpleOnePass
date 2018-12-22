import string
import sys

from src.CInput import CInput
from src.token import Token


class CLexer:

    def __init__(self, input):
        
        self.input_ptr = -1
        self.line_no = 0
        self.line_pos = 0
        self.token_value = None    
        self.tokens = [] 
        self.input = input

    def tokenizer(self, input):
        
        i = 1
        c = input.getchar()

        while not input.NO_MORE_CHARS():

            # ignore whitespace
            if c in input.whitespace:
                while c in input.whitespace:
                    if c in input.newline:
                        input.Lineno += 1
                        input.Linepos = 0
                        #print(f'newline')
                    i += 1
                    c = input.getchar()
                #print(f'whitespace')

            # comment
            elif c in input.comment_marker:
                match = c
                i += 1                
                c = input.getchar()
                while c not in input.newline:
                    match += c                                
                    i += 1                
                    c = input.getchar()
                print(f'comment : {match}')

            # html comment <!-- -->
            elif c in input.LESS_THAN:
                match = c
                i += 1                

                if (chr(input.ii_look(1)) == input.EXCLAMATION):
                    print(f'ii_look found EXCLAMATION')
                else:
                    print(f'{i} - {c}')            
                    i += 1
                    c = input.getchar()
                    continue


                c = input.getchar()
                if c in input.EXCLAMATION:
                    match += c
                    i += 1
                    
                    c = input.getchar()
                    if c in input.DASH:
                        match += c
                        i += 1                

                        c = input.getchar()
                        if c in input.DASH:
                            match += c
                            i += 1      

                            c = input.getchar()
                            while c not in input.GREATER_THAN:
                                match += c                                
                                i += 1                
                                c = input.getchar()
                        print(f'HTML comment : {match}')

            # identifier token
            elif c.isalpha(): #in string.ascii_letters:
                match = c
                i += 1    
                c = input.getchar()

                while c.isalnum(): #in string.ascii_letters:
                    match += c
                    i += 1
                    c = input.getchar()               

                #print(f'id : {match}')
                token = Token(Token.IDENT, match, input.Lineno, self.line_no, self.line_pos)
                self.tokens.append(token)

            # number
            elif (c in string.digits):
                match = c
                i += 1            
                Token.token_value = int(c) - 0
                c = input.getchar()
                
                while(c in string.digits):                    
                    match += c
                    i += 1 
                    Token.token_value = Token.token_value * 10 + int(c) - 0
                    c = input.getchar()
                token = Token(Token.NUM, c, input.Lineno, self.line_no, self.line_pos)
                self.tokens.append(token)                   
                #print(f'number : {match}')
                # return Token.NUM                

            else:
                print(f'{i} - {c}')            
                i += 1
                c = input.getchar()

        # end of file token
        token = Token(Token.EOF, c, None, self.line_no, self.line_pos)
        self.tokens.append(token)

        return self.tokens                


if __name__ == '__main__':
    
    clexer = CLexer()
    input = CInput()
    input.ii_ii(input.open_funct, input.close_funct, input.read_funct)
    input.ii_newfile('./src/test_files/web.config')
    i = 1
    c = input.getchar()
