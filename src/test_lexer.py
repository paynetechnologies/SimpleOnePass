import unittest
import globall as G

class TestLexer(unittest.TestCase):
    """ Test lexer variables """
    
    def test_01_create_entry(self):
        e = G.Entry("lexptr",0)
        print(f'Entry : {e.lexptr, e.token }')
        self.assertEqual(e.lexptr,'lexptr')
        self.assertEqual(e.token, 0)

    def test_02_add_entry_to_symbolTable(self):
        e = G.Entry("lexptr",0)
        G.SYMBOL_TABLE.append(e)
        print(f'SYMBOL_TABLE : {G.SYMBOL_TABLE[0].lexptr, G.SYMBOL_TABLE[0].token }')
        self.assertEqual(G.SYMBOL_TABLE[0].lexptr, 'lexptr')
        self.assertEqual(G.SYMBOL_TABLE[0].token, 0)

if __name__ == '__main__':
    unittest.main()