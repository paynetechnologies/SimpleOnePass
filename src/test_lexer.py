import unittest
import globals as globals

class Test_Lexer(unittest.TestCase):
    """ Test lexer variables """

    def setUp(self):
        self.e = globals.Entry("lex",0)

    def tearDown(self):
        return super().tearDown()

    def test_01_add_entry_to_symbolTable(self):
        globals.SYMBOL_TABLE.append(self.e)
        print(f'SYMBOL_TABLE : {globals.SYMBOL_TABLE[0].lex, globals.SYMBOL_TABLE[0].token }')
        self.assertEqual(globals.SYMBOL_TABLE[0].lex, 'lex')
        self.assertEqual(globals.SYMBOL_TABLE[0].token, 0)

if __name__ == '__main__':
    unittest.main()