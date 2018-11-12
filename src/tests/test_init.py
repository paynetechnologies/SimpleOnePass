import unittest
from src.constants import constants, entry
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
        [self.symTbl.st_insert(k, v) for k,v in Test_init.keywords.items()]

        for sym in constants.SYMBOL_TABLE:
            print(f'Token : {sym.token} - Value : {sym.lexeme}')

    def test_init_symbol_table(self):
        '''Loads keywords into SYMBOL_TABLE'''        
        [print(f'Token : {t} - Lexeme : {l}') for t, l in Test_init.keywords.items()]
        
        self.symTbl.st_insert('MOD', 'MOD')
        self.symTbl.st_lookup('MOD')
        self.symTbl.st_insert('Howard', constants.ID)
        self.symTbl.st_lookup('Howard')
        self.symTbl.st_insert('Payne', constants.ID)    
        self.symTbl.st_lookup('Payne')
        print('done')
        
        for sym in constants.SYMBOL_TABLE:
            print(f'Token : {sym.token} - Value : {sym.lexeme}')

if __name__ == '__main__':
    unittest.main()
    # ti = Test_init()
    # ti.setup()
    # ti.test_init_symbol_table()