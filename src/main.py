import sys
from src.parser import parser
from src.init import init
from CInput import CInput



if __name__ == '__main__':
    
    input = CInput()
    ii_io(open_funct, close_funct, read_funct)
    input.ii_newfile('./src/test_files/web.config') 
    #input.ii_newfile('./src/test_files/abcdefg.txt') 

    i = 1
    c = input.getchar()

    while not input.NO_MORE_CHARS():
        # ignore whitespace
        if c in input.whitespace:
            while c in input.whitespace:
                if c in input.newline:
                    input.Lineno += 1
                    input.Linepos = 0
                    print(f'newline')
                i += 1
                c = input.getchar()
            print(f'whitespace')

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

            print(f'id : {match}')
            
        # number
        elif (c in string.digits):
            match = c
            i += 1            
            #Token.token_value = int(char) - 0
            c = input.getchar()
            
            while(c in string.digits):                    
                match += c
                i += 1 
                #Token.token_value = Token.token_value * 10 + int(char) - 0
                c = input.getchar()
            # token = Token(Token.NUM, char, self.lines[self.line_no], self.line_no, self.line_pos)
            # self.tokens.append(token)                   
            # return Token.NUM
            print(f'number : {match}')

        else:
            print(f'{i} - {c}')            
            i += 1
            c = input.getchar()
