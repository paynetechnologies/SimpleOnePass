import sys
from src.error import error_message
from src.constants import constants, entry
from src.lexer import lexer
from src.emitter import emit

class parser(object):

    lookahead = 0

    def __init__(self, input):
        self.input = input
        self.lex = lexer()
        self.lex.loadBuffer(self.input)

    def match(self, t):
        
        if (parser.lookahead == t):
            parser.lookahead = self.lex.tokenizer()
        else:
            error_message("syntax error")

    def parse(self):
        # lookahead = token
        parser.lookahead = self.lex.tokenizer()
        while (parser.lookahead != constants.DONE):
            self.expr() 
            #self.match(';') separtor between lines???


    def expr(self):

        self.term()
        
        while(True):
            if (parser.lookahead == '+' or parser.lookahead == '-'):
                t = parser.lookahead
                self.match(t)
                self.term()
                emit(t, None)
            else:
                return

    def term(self ):

        self.factor()

        while (True):

            if (parser.lookahead in ['*','/','DIV','MOD']):
                t = parser.lookahead
                self.match(t)
                self.factor()
                emit(t, None)

            else:
                return


    def factor(self):
        
        if (parser.lookahead == "("):
            self.match("(")
            self.expr()
            self.match(")")

        elif (parser.lookahead == constants.NUM):
            emit(constants.NUM, constants.token_value)
            self.match(constants.NUM)

        elif (parser.lookahead == constants.ID):
            emit(constants.ID, constants.token_value)
            self.match(constants.ID)

        else:
            error_message(constants.line_no,"syntax error")

