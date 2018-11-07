import sys
import src.error
from src.constants import constants, entry
from src.lexer import lex_manager


def parse():
    lookahead = lex_manager.lex_analysis()
    while (lookahead != DONE):
        expr(); 
        match(';')

def expr():
    term()
    
    while(True):
        switch (lookahead):
        case '+':
        case '-':
            t = lookahead
            match(lookahead)
            term()
            emit(t, None)
            continue;
        default:
            return

def term():
    factor()

    while (True)            
        switch (lookahead):
        case '*':
        case '/':
        case 'DIV':
        case 'MOD':                
            t = lookahead
            match(lookahead)
            factor()
            emit(t, None)
            continue;
        default:
            return


def factor():
    switch(lookahead)            :

        case "(":
            match("(")
            expr()
            match")"
            break;

        case NUM:
            match(NUM, tokenval)
            match(NUM)
            break;

        case ID:

        default:
            error("syntax error")

def match(t):
    if (lookahead ==t):
        lookahead = lex_manager.lex_analysis()
    else
        error("syntax error")