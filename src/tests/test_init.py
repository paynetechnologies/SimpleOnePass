import unittest
from src.token import Token
from src.symbol_table import Entry, SymbolTable

class Test_Init(unittest.TestCase):
    """ Test init """
    
    keywords = {'DIV' : 'DIV', 'MOD' : 'MOD'}
    
    def __init__(self, *args, **kwargs):
        super(Test_Init, self).__init__(*args, **kwargs)
        self.symTbl = None


    def setUp(self):
        '''Loads keywords into SYMBOL_TABLE'''
        print('\n### Test_Init::setUp - Load keywords into SYMBOL_TABLE')   
    
        SymbolTable.symbol_table=[]
        SymbolTable.last_entry = -1
        [print(f'Token : {t} -> Lexeme : {l}') for t, l in Test_Init.keywords.items()]

        [SymbolTable.add(k, v) for k,v in Test_Init.keywords.items()]

        self.Dump_Symbol_Table()
        

    def test_01_init_symbol_table_add(self):
        '''Add Identifiers SYMBOL_TABLE'''   
        print('\n*** Test_Init::test_init_01_symbol_table_add') 
       
        SymbolTable.add(Token.ID,'Howard' )
        self.assertEqual(SymbolTable.last_entry, 2)
        
        SymbolTable.add(Token.ID, 'Payne')
        self.assertEqual(SymbolTable.last_entry, 3)
            
        #self.Dump_Symbol_Table()


    def test_02_init_symbol_table_lookup(self):
        '''Lookup identifiers in SYMBOL_TABLE'''   
        print('\n\n*** Test_Init::test_02_init_symbol_table_lookup') 

        # [print(f'Token : {t} -> Lexeme : {l}') for t, l in Test_Init.keywords.items()]
        
        found = SymbolTable.lookup('Howard')        
        if not found:
            SymbolTable.add(Token.ID,'Howard' )
        found = SymbolTable.lookup('Howard')        
        self.assertEqual(found, 2)      

        found = SymbolTable.lookup('Payne')
        if not found:
            SymbolTable.add(Token.ID, 'Payne')  
        found = SymbolTable.lookup('Payne')
        self.assertEqual(found, 3)   

        self.Dump_Symbol_Table()

    def Dump_Symbol_Table(self):
        print('\n<<Dump Symbol Table>>')
        for sym in SymbolTable.symbol_table:
            print(f'Token : {sym.token} -> Lexeme : {sym.lexeme}')
        #[print(f'Token : {t} -> Lexeme : {l}') for t, l in SymbolTable.symbol_table]


if __name__ == '__main__':
    unittest.main()
