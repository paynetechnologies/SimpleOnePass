import unittest
from src.constants import constants, entry

class Test_Global(unittest.TestCase):
    """ Test global variables """
    
    def test_01_create_entry(self):
        e = entry("lexeme",0)
        print(f'\nEntry : {e.lexeme, e.token }')
        self.assertEqual(e.lexeme,'lexeme')
        self.assertEqual(e.token, 0)

    def test_02_add_entry_to_symbolTable(self):
        e = entry("lexeme",0)
        constants.SYMBOL_TABLE.append(e)
        print(f'\nSYMBOL_TABLE : {constants.SYMBOL_TABLE[0].lexeme, constants.SYMBOL_TABLE[0].token }')
        self.assertEqual(constants.SYMBOL_TABLE[0].lexeme, 'lexeme')
        self.assertEqual(constants.SYMBOL_TABLE[0].token, 0)

if __name__ == '__main__':
    unittest.main()