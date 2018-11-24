import unittest
from src.token import Token
from src.symbol_table import Entry, SymbolTable

class Test_Symbol_Table(unittest.TestCase):
    """ Test Symbol_Table variables """
    
    @classmethod
    def setUpClass(self):
        
        print('\n\n*** Test_Symbol_Table')
        SymbolTable.symbol_table = []
        self.e1 = Entry(Token.ID, value="identifier")
        self.e2 = Entry(Token.KEYWORD, value="while")

    @classmethod
    def tearDown(self):
        return super().tearDown(self)

    def test_01_append_entry_to_symbolTable(self):
        SymbolTable.add_entry(self.e1)
        print(f'\nSYMBOL_TABLE : {SymbolTable.symbol_table[0].token, SymbolTable.symbol_table[0].lexeme }')
        self.assertEqual(SymbolTable.symbol_table[0].token, Token.ID)
        self.assertEqual(SymbolTable.symbol_table[0].lexeme, 'identifier')
        SymbolTable.last_entry = 0

    def test_02_add_entry_to_symbolTable(self):
        SymbolTable.add_entry(self.e2)
        print(f'\nSYMBOL_TABLE : {SymbolTable.symbol_table[1].token, SymbolTable.symbol_table[1].lexeme}')
        self.assertEqual(SymbolTable.symbol_table[1].token, Token.KEYWORD)        
        self.assertEqual(SymbolTable.symbol_table[1].lexeme, 'while')

if __name__ == '__main__':
    unittest.main()

