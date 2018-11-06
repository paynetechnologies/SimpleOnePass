import unittest
from src.constants import constants, entry

class Test_Global(unittest.TestCase):
    """ Test global variables """
    
    def test_01_create_entry(self):
        e = entry("lex",0)
        print(f'\nEntry : {e.lex, e.token }')
        self.assertEqual(e.lex,'lex')
        self.assertEqual(e.token, 0)

    def test_02_add_entry_to_symbolTable(self):
        e = entry("lex",0)
        constants.SYMBOL_TABLE.append(e)
        print(f'\nSYMBOL_TABLE : {constants.SYMBOL_TABLE[0].lex, constants.SYMBOL_TABLE[0].token }')
        self.assertEqual(constants.SYMBOL_TABLE[0].lex, 'lex')
        self.assertEqual(constants.SYMBOL_TABLE[0].token, 0)

if __name__ == '__main__':
    unittest.main()