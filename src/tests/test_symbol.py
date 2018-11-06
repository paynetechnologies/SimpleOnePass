import unittest
from src.constants import constants, entry

class Test_Symbol_Table(unittest.TestCase):
    """ Test Symbol_Table variables """
    
    def setUp(self):
        self.e = entry("lex",0)

    def tearDown(self):
        return super().tearDown()
    
    def test_01_create_entry(self):
        self.assertEqual(self.e.lex,'lex')
        self.assertEqual(self.e.token, 0)

    def test_02_append_entry_to_symbolTable(self):
        constants.SYMBOL_TABLE.append(self.e)
        print(f'\nSYMBOL_TABLE : {constants.SYMBOL_TABLE[0].lex, constants.SYMBOL_TABLE[0].token }')
        self.assertEqual(constants.SYMBOL_TABLE[0].lex, 'lex')
        self.assertEqual(constants.SYMBOL_TABLE[0].token, 0)

    def test_03_add_entry_to_symbolTable(self):
        constants.SYMBOL_TABLE[0].insert = self.e
        print(f'\nSYMBOL_TABLE : {constants.SYMBOL_TABLE[0].lex, constants.SYMBOL_TABLE[0].token }')
        self.assertEqual(constants.SYMBOL_TABLE[0].lex, 'lex')
        self.assertEqual(constants.SYMBOL_TABLE[0].token, 0)        

if __name__ == '__main__':
    unittest.main()