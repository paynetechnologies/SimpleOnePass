import sys
from src.error import error_message
from src.constants import constants, entry
from src.lexer import lexer
from src.emitter import emit

class parser(object):
    
    def __init__(self, input):
        self.input = input
        self.lex = lexer()
        self.lex.loadBuffer(self.input)

    def match(self, t, lookahead):
        
        if (lookahead == t):
            lookahead = self.lex.tokenizer()
        else:
            error_message("syntax error")

    def parse(self):
        # lookahead = token
        lookahead = self.lex.tokenizer()
        while (lookahead != constants.DONE):
            self.expr(lookahead) 
            self.match(';', lookahead)


    def expr(self, lookahead):

        self.term(lookahead)
        
        while(True):
            if (lookahead == '+' or lookahead == '-'):
                t = lookahead
                self.match(t, lookahead)
                self.term(lookahead)
                emit(t, None)
            else:
                return

    def term(self, lookahead):

        self.factor(lookahead)

        while (True):

            if (lookahead in ['*','/','DIV','MOD']):
                t = lookahead
                self.match(t, lookahead)
                self.factor(lookahead)
                emit(t, None)

            else:
                return


    def factor(self, lookahead):
        
        if (lookahead == "("):
            self.match("(", lookahead)
            self.expr(lookahead)
            self.match(")", lookahead)

        elif (lookahead == constants.NUM):
            emit(constants.NUM, 'tokenval')
            self.match(constants.NUM, lookahead)

        elif (lookahead == constants.ID):
            emit(constants.ID, 'tokenval')
            self.match(constants.ID, lookahead)

        else:
            error_message("syntax error")



    # def f(x):
    #     return {
    #         'a': 1,
    #         'b': 2
    #     }.get(x, default) 

    # choices = {'a': 1, 'b': 2}
    # result = choices.get(key, 'default')

    # expr_choices = {'+': func(), '-': func2() , 'default': return }
    # result = expr_choices.get(key, 'default')
