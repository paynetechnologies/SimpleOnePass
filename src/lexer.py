import sys
import array as arr
from src.symbol_table import lookup, insert
from src.constants import constants, entry
from src.error import error

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
        print(f'Loading buffer...')
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
    def isNewLine(cls, char):
        if (char == "\n"):
            return True
        return False

    @classmethod
    def isWhiteSpace(cls, char):
        if (char == " " or char =="\t"):
            return True
        return False

    def tokenizer(self):
        char = ""
        while(True):
            char = self.getchar()

            if (lexer.isWhiteSpace(char)):
                while(lexer.isWhiteSpace(char)):
                    char = self.getchar()
                constants.TOKEN_VALUE = constants.WHITESPACE
                return constants.WHITESPACE

            elif (lexer.isNewLine(char)):
                while(lexer.isNewLine(char)):
                    constants.LINE_NUMBER += 1                    
                    char = self.getchar()
                constants.TOKEN_VALUE = constants.NEWLINE
                return constants.NEWLINE

            elif (char.isdigit()):
                constants.TOKEN_VALUE = int(char) - 0
                char = self.getchar()
                while(char.isdigit()):
                    constants.TOKEN_VALUE = constants.TOKEN_VALUE * 10 + int(char) - 0
                    char = self.getchar()

                if (char != self.EOF):
                    self.ungetchar()                    
            
                self.b += 1
                if (self.b >= constants.BSIZE):
                    error("compiler error")

                self.lexbuf[self.b] = constants.TOKEN_VALUE
                
                self.b += 1
                self.lexbuf[self.b] = constants.EOS

                print(f'isdigit : {self.lexbuf[self.b-1]}')
                return constants.NUM

            elif (char.isalpha()):
                self.b = 0
                while (char.isalnum()):
                    self.lexbuf[self.b] = char
                    char = self.getchar()
                    self.b += 1
                    if (self.b >= constants.BSIZE):
                        error("compiler error")

                self.lexbuf[self.b] = constants.EOS

                if (char != self.EOF):
                    self.ungetchar()
                # create string from slice of list
                lexeme = ''.join(self.lexbuf[:self.b])
                p = lookup(lexeme)

                if (p == None):
                    p = insert(lexeme, constants.ID)
                constants.TOKEN_VALUE = p
                
                return constants.SYMBOL_TABLE[p].token
            
            elif (char == self.EOF):
                return constants.DONE

            elif ( char in ["+", "-", "*", "/"] ):
                return constants.OPERATOR

            else:
                constants.TOKEN_VALUE = constants.NONE
                return char

if (__name__ == "__main__"):
    l = lexer()
    l.loadBuffer("   a")
    l.tokenizer()