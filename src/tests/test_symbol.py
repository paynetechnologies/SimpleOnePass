import unittest
from src.token import Token
from src.symbol_table import entry, symbol_table

class Test_Symbol_Table(unittest.TestCase):
    """ Test Symbol_Table variables """
    
    @classmethod
    def setUpClass(self):
        print('\n\n Test_Symbol_Table')
        symbol_table.SYMBOL_TABLE=[]
        self.e1 = entry(token=1, value="lexeme1")
        self.e2 = entry(token=2, value="lexeme2")

    @classmethod
    def tearDown(self):
        return super().tearDown(self)

    def test_01_append_entry_to_symbolTable(self):
        symbol_table.SYMBOL_TABLE.append(self.e1)
        print(f'\nSYMBOL_TABLE : {symbol_table.SYMBOL_TABLE[0].token, symbol_table.SYMBOL_TABLE[0].lexeme }')
        self.assertEqual(symbol_table.SYMBOL_TABLE[0].token, 1)
        self.assertEqual(symbol_table.SYMBOL_TABLE[0].lexeme, 'lexeme1')
        symbol_table.last_entry = 0

    def test_02_add_entry_to_symbolTable(self):
        symbol_table.addEntry(self.e2)
        print(f'\nSYMBOL_TABLE : {symbol_table.SYMBOL_TABLE[1].token, symbol_table.SYMBOL_TABLE[1].lexeme}')
        self.assertEqual(symbol_table.SYMBOL_TABLE[1].token, 2)        
        self.assertEqual(symbol_table.SYMBOL_TABLE[1].lexeme, 'lexeme2')

if __name__ == '__main__':
    unittest.main()

