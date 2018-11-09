import sys
import array as arr
from src.error import error
from src.symbol_table import lookup, insert
from src.constants import constants, entry

constants.LINE_NUMBER = 1
constants.TOKEN_VALUE = None

inputBuffer = ""

class lexer():

    def __init__(self):
        #self.inputBuffer = input
        self.lookahead = ""
        self.ptr = 0
        self.EOF = ';'
        self.lexbuf = [None] * constants.BSIZE
        self.p = self.b = -1

    def loadBuffer(self, input):
        self.inputBuffer = input

    def getchar(self):
        c = self.inputBuffer[self.ptr]
        if (c == ';'):
            constants.EOF = True
        self.ptr += 1
        return c

    def ungetchar(self):
        self.ptr -= 1

    @classmethod
    def isNewLine(cls, t):
        if (t == "\n"):
            return True
        return False

    @classmethod
    def isWhiteSpace(cls, t):
        if (t == " " or t =="\t"):
            return True
        return False

    def tokenizer(self):
        t=""
        while(True):
            t = self.getchar()

            if (lexer.isWhiteSpace(t)):
                while(lexer.isWhiteSpace(t)):
                    t = self.getchar()
                constants.TOKEN_VALUE = constants.WHITESPACE
                return constants.WHITESPACE

            elif (lexer.isNewLine(t)):
                while(lexer.isNewLine(t)):
                    constants.LINE_NUMBER += 1                    
                    t = self.getchar()
                constants.TOKEN_VALUE = constants.NEWLINE
                return constants.NEWLINE

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
                    error("compiler error")

                self.lexbuf[self.b] = constants.TOKEN_VALUE
                
                self.b += 1
                self.lexbuf[self.b] = constants.EOS

                print(f'isdigit : {self.lexbuf[self.b-1]}')
                return constants.NUM

            elif (t.isalpha()):
                self.b = 0
                while (t.isalnum()):
                    self.lexbuf[self.b] = t
                    t = self.getchar()
                    self.b += 1
                    if (self.b >= constants.BSIZE):
                        error("compiler error")

                self.lexbuf[self.b] = constants.EOS

                if (t != self.EOF):
                    self.ungetchar()
                # create string from slice of list
                lexeme = ''.join(self.lexbuf[:self.b])
                p = lookup(lexeme)

                if (p == None):
                    p = insert(lexeme, constants.ID)
                constants.TOKEN_VALUE = p
                
                return constants.SYMBOL_TABLE[p].token
            
            elif (t == self.EOF):
                return constants.DONE

            elif ( t in ["+", "-", "*", "/"] ):
                return constants.OPERATOR

            else:
                constants.TOKEN_VALUE = constants.NONE
                return t

if (__name__ == "__main__"):
    l = lexer("   a")
    l.tokenizer()