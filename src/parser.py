import sys
import src.error
from src.constants import constants, entry
from src.lexer import lex_manager


def parse():
    lookahead = lex_manager.lex_analysis()
    while (lookahead != DONE):
        expr(lookahead); 
        match(';')


def expr(lookahead):

    term(lookahead)
    
    while(True):
        if (lookahead == '+' or lookahead == '-'):
            t = lookahead
            match(t, lookahead)
            term(lookahead)
            emit(t, None)
        else:
            return

def term(lookahead):

    factor(lookahead)

    while (True):

        if (lookahead in ['*','/','DIV','MOD']):
            t = lookahead
            match(t, lookahead)
            factor(lookahead)
            emit(t, None)

        else:
            return


def factor(lookahead):
    
    if (lookahead == "("):
        match("(", lookahead)
        expr(lookahead)
        match(")", lookahead)

    elif (lookahead == NUM):
        emit(NUM, tokenval)
        match(NUM, lookahead)

    elif (lookahead == ID):
        emit(ID, tokenval)
        match(ID, lookahead)

    else:
        error("syntax error")

def match(t, lookahead):
    
    if (lookahead == t):
        lookahead = lex_manager.lex_analysis()
    else:
        error("syntax error")



# def f(x):
#     return {
#         'a': 1,
#         'b': 2
#     }.get(x, default) 

# choices = {'a': 1, 'b': 2}
# result = choices.get(key, 'default')

# expr_choices = {'+': func(), '-': func2() , 'default': return }
# result = expr_choices.get(key, 'default')
