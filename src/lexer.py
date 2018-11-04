import sys
import error
import symbol
from src.globals import constants, entry

constants.LINE_NUMBER = 1
constants.TOKEN_VALUE = None

class lexman(object):

    def __init__(self, inputStr):
        self.inputString = inputStr
        self.lookahead = ""
        self.ptr = 0
        self.EOF = False
        self.lexbuf = [None] * constants.BSIZE
        self.p = self.b = -1

    def getchar(self):
        c = self.inputString[self.ptr]
        if (c == ';'):
            constants.EOF = True
        self.ptr += 1
        return c

    def ungetchar(self):
        self.ptr -= 1

    def isNewLine(self, t):
        if (t == "\n"):
            return True
        return False

    def isWhiteSpace(self, t):
        if (t == "" or t =="\t"):
            return True
        return False

    def lex(self):
        t=""
        while(True):
            t = self.getchar()

            if (self.isWhiteSpace(t)):
                pass

            elif (self.isNewLine(t)):
                constants.LINE_NUMBER += 1
                      
            elif (t.isdigit()):
                constants.TOKEN_VALUE = int(t) - 0
                t = self.getchar()
                while(t.isdigit()):
                    constants.TOKEN_VALUE = constants.TOKEN_VALUE * 10 + int(t) - 0
                    t = self.getchar()

                if (t != self.EOF):
                    self.ungetchar()                    
            
                self.b += 1
                if (self.b >= constants.BSIZE):
                    error.error("compiler error")

                self.lexbuf[self.b] = constants.TOKEN_VALUE
                
                self.b += 1
                self.lexbuf[self.b] = constants.EOS

                print(f'isdigit : {self.lexbuf[self.b-1]}')
                return constants.NUM

            elif (t.isalpha()):
                while (t.isalnum()):
                    self.b += 1
                    self.lexbuf[self.b] = t
                    t = self.getchar()
                    self.b += 1
                    if (self.b >= constants.BSIZE):
                        error.error("compiler error")

                self.lexbuf[self.b] = constants.EOS

                if (t != self.EOF):
                    self.ungetchar()
                
                p = symbol.lookup(self.lexbuf)
                
                if (p == None):
                    p = symbol.insert(self.lexbuf, constants.ID)
                constants.TOKEN_VALUE = p
                
                return constants.SYMBOL_TABLE[p].token
            
            elif (t == self.EOF):
                return constants.DONE

            else:
                constants.TOKEN_VALUE = constants.NONE
                return t

if (__name__ == "__main__"):
    l = lexman("12345 + 5 - 2;")
    l.lex()