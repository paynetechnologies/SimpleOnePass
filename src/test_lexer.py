import unittest
import globall as G

class Test_Lexer(unittest.TestCase):
    """ Test lexer variables """

    def setUp(self):
        self.e = G.Entry("lex",0)

    def tearDown(self):
        return super().tearDown()

    def test_01_add_entry_to_symbolTable(self):
        G.SYMBOL_TABLE.append(self.e)
        print(f'SYMBOL_TABLE : {G.SYMBOL_TABLE[0].lex, G.SYMBOL_TABLE[0].token }')
        self.assertEqual(G.SYMBOL_TABLE[0].lex, 'lex')
        self.assertEqual(G.SYMBOL_TABLE[0].token, 0)

if __name__ == '__main__':
    unittest.main()