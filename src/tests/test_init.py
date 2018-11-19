import unittest
from src.token import Token
from src.symbol_table import entry, symbol_table

class Test_init(unittest.TestCase):
    """ Test init """
    
    keywords = {'DIV' : 'DIV', 'MOD' : 'MOD'}
    
    def __init__(self, *args, **kwargs):
        super(Test_init, self).__init__(*args, **kwargs)
        self.symTbl = None

    def setUp(self):
        '''Loads keywords into SYMBOL_TABLE'''
        for (token, value) in Test_init.keywords.items():
            print (f'Token : {token} - Value : {value}')    

        self.symTbl = symbol_table()
        [self.symTbl.add(k, v) for k,v in Test_init.keywords.items()]

        for sym in symbol_table.SYMBOL_TABLE:
            print(f'Token : {sym.token} - Value : {sym.lexeme}')

    def test_init_symbol_table(self):
        '''Loads keywords into SYMBOL_TABLE'''        
        [print(f'Token : {t} - Lexeme : {l}') for t, l in Test_init.keywords.items()]
        
        self.symTbl.add('MOD', 'MOD')
        self.symTbl.lookup('MOD')
        self.symTbl.add('Howard', Token.ID)
        self.symTbl.lookup('Howard')
        self.symTbl.add('Payne', Token.ID)    
        self.symTbl.lookup('Payne')
        print('done')
        
        for sym in symbol_table.SYMBOL_TABLE:
            print(f'Token : {sym.token} - Value : {sym.lexeme}')

if __name__ == '__main__':
    unittest.main()
    # ti = Test_init()
    # ti.setup()
    # ti.test_init_symbol_table()