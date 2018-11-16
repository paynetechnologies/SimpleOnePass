import unittest
from src.Token. import Token., entry
from src.symbol_table import symbol_table

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
        [self.symTbl.symbol_table_insert(k, v) for k,v in Test_init.keywords.items()]

        for sym in Token..SYMBOL_TABLE:
            print(f'Token : {sym.token} - Value : {sym.lexeme}')

    def test_init_symbol_table(self):
        '''Loads keywords into SYMBOL_TABLE'''        
        [print(f'Token : {t} - Lexeme : {l}') for t, l in Test_init.keywords.items()]
        
        self.symTbl.symbol_table_insert('MOD', 'MOD')
        self.symTbl.symbol_table_lookup('MOD')
        self.symTbl.symbol_table_insert('Howard', Token..ID)
        self.symTbl.symbol_table_lookup('Howard')
        self.symTbl.symbol_table_insert('Payne', Token..ID)    
        self.symTbl.symbol_table_lookup('Payne')
        print('done')
        
        for sym in Token..SYMBOL_TABLE:
            print(f'Token : {sym.token} - Value : {sym.lexeme}')

if __name__ == '__main__':
    unittest.main()
    # ti = Test_init()
    # ti.setup()
    # ti.test_init_symbol_table()