import unittest
import globall as G
import symbol

class Test_init(unittest.TestCase):
    """ Test init """

    def test_init(self):
        keywords = {'div' : 'DIV', 'mod' : 'MOD'}
        '''Loads keywords into SYMBOL_TABLE'''
        #G.SYMBOL_TABLE = {symbol.insert(lex, tok) for lex,tok in keywords}
        #dict_variable = {key:value for (key,value) in dictonary.items()}
        print(f'TOK : {tok} - LEX : {lex}' for (tok, lex) in keywords)        
        
        for sym in G.SYMBOL_TABLE:
            print(f'TOK : {sym.token} - LEX : {sym.lex}')
            assert("unknown")

def init():
    '''Loads keywords into SYMBOL_TABLE'''
    keywords = {'div' : 'DIV', 'mod' : 'MOD'}
    G.SYMBOL_TABLE = {symbol.insert(k, v) for k,v in keywords.items()}

    #G.SYMBOL_TABLE = {symbol.insert(lex, tok) for lex,tok in keywords}
    #dict_variable = {key:value for (key,value) in dictonary.items()}
    for (k,v) in keywords.items():
        print (f'k {k} - v {v}')    
    #x,y = {lex:tok for (lex, tok) in keywords.items()}
    #print (f'x {x} - y {y}')
    #x1 = {lex:tok for (lex, tok) in keywords.items()}
    #print (f'x1 {x1}')

    #print(f' LEX : {l} - TOK : {t} ') 
    
    # for sym in G.SYMBOL_TABLE:
    #     print(f'TOK : {sym.token} - LEX : {sym.lex}')
    #     assert("unknown")

if __name__ == '__main__':
    #unittest.main()
    init()
    