import sys
from src.error import lex_error_message
from src.symbol_table import entry
from src.lexer import lexer
from src.emitter import emit
from src.token import Token

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
            lex_error_message(Token.line_no,"match syntax error")

    def parse(self):
        parser.lookahead = self.lex.tokenizer()
        
        while (parser.lookahead != Token.EOF):
            self.expr() 

        # on EOF, print the tokens    
        for token in self.lex.tokens:
            print(token)


    def expr(self):

        self.term()
        
        while(True):

            if (parser.lookahead == '+' or parser.lookahead == '-'):
                t = parser.lookahead
                self.match(t); 
                self.term(); 
                emit(t, Token.NONE)

            else:
                return

    def term(self ):

        self.factor()

        while (True):

            if (parser.lookahead in ['*','/','DIV','MOD']):
                t = parser.lookahead
                self.match(t)
                self.factor()
                emit(t, Token.NONE)

            else:
                return


    def factor(self):
        
        if (parser.lookahead == "("):
            self.match("(") 
            self.expr()
            self.match(")")

        elif (parser.lookahead == Token.NUM):
            emit(Token.NUM, Token.token_value) ; 
            self.match(Token.NUM)

        elif (parser.lookahead == Token.ID):
            emit(Token.ID, Token.token_value); 
            self.match(Token.ID)
        else:
            lex_error_message(self.lex.line_no,"factor syntax error")

