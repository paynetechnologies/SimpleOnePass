import unittest
from src.globals import constants, entry

class Test_Lexer(unittest.TestCase):
    """ Test lexer variables """

    def setUp(self):
        self.e = entry("lex",0)

    def tearDown(self):
        return super().tearDown()

    def test_01_add_entry_to_symbolTable(self):
        constants.SYMBOL_TABLE.append(self.e)
        print(f'SYMBOL_TABLE : {constants.SYMBOL_TABLE[0].lex, constants.SYMBOL_TABLE[0].token }')
        self.assertEqual(constants.SYMBOL_TABLE[0].lex, 'lex')
        self.assertEqual(constants.SYMBOL_TABLE[0].token, 0)

if __name__ == '__main__':
    unittest.main()