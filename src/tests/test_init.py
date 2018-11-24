import unittest
from src.token import Token
from src.symbol_table import entry, symbol_table

class Test_Init(unittest.TestCase):
    """ Test init """
    
    keywords = {'DIV' : 'DIV', 'MOD' : 'MOD'}
    
    def __init__(self, *args, **kwargs):
        super(Test_Init, self).__init__(*args, **kwargs)
        self.symTbl = None


    def setUp(self):
        '''Loads keywords into SYMBOL_TABLE'''
        print('\nTest_Init::setUp - Load keywords into SYMBOL_TABLE')   
    
        self.symTbl = symbol_table()
        self.symTbl.SYMBOL_TABLE = []
        [self.symTbl.insert(k, v) for k,v in Test_Init.keywords.items()]

        # for sym in symbol_table.SYMBOL_TABLE:
        #     print(f'Token : {sym.token} -> Lexeme : {sym.lexeme}')
        

    def test_01_init_symbol_table_insert(self):
        '''Loads keywords into SYMBOL_TABLE'''   
        print('\nTest_Init::test_init_01_symbol_table_insert') 

        # [print(f'Token : {t} -> Lexeme : {l}') for t, l in Test_Init.keywords.items()]
        
        found = self.symTbl.lookup('Howard')        
        if not found:
            self.symTbl.insert(Token.ID,'Howard' )
        
        found = self.symTbl.lookup('Payne')
        if not found:
            self.symTbl.insert(Token.ID, 'Payne')    
            
        # for sym in symbol_table.SYMBOL_TABLE:
        #     print(f'Token : {sym.token} -> Lexeme : {sym.lexeme}')

    def test_02_init_symbol_table_lookup(self):
        '''Lookupo in SYMBOL_TABLE'''   
        print('\n\nTest_Init::test_02_init_symbol_table_lookup') 

        # [print(f'Token : {t} -> Lexeme : {l}') for t, l in Test_Init.keywords.items()]
        
        found = self.symTbl.lookup('Howard')
        self.assertNotEqual(found, None)      
       
        found = self.symTbl.lookup('Payne')
        self.assertNotEqual(found, None)      

if __name__ == '__main__':
    unittest.main()
