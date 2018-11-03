import sys
import error
import symbol
import globals

globals.LINE_NUMBER = 1
globals.TOKEN_VALUE = None

class lexman(object):

    def __init__(self, inputStr):
        self.inputString = inputStr
        self.lookahead = ""
        self.ptr = 0
        self.EOF = False
        self.lexbuf = [None] * globals.BSIZE

    def getchar(self):
        c = self.inputString[self.ptr]
        if (c == ';'):
            globals.EOF = True
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
                globals.LINE_NUMBER += 1

            elif (t.isdigit()):
                self.ungetchar()
                print(f't : {t}')
                return globals.NUM

            elif (t.isalpha()):
                p = b = 0
                while (t.isalnum()):
                    self.lexbuf[b] = t
                    t = self.getchar()
                    b += 1
                    if (b >= globals.BSIZE):
                        error.error("compiler error")

                self.lexbuf[b] = globals.EOS

                if (t != self.EOF):
                    self.ungetchar()
                
                p = symbol.lookup(self.lexbuf)
                
                if (p == None):
                    p = symbol.insert(self.lexbuf, globals.ID)
                globals.TOKEN_VALUE = p
                
                return globals.SYMBOL_TABLE[p].token
            
            elif (t == self.EOF):
                return globals.DONE

            else:
                globals.TOKEN_VALUE = globals.NONE
                return t

if (__name__ == "__main__"):
    l = lexman("A + B = C;")
    l.lex()