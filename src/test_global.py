import unittest
import globall as G

class Test_Global(unittest.TestCase):
    """ Test global variables """
    
    def test_01_create_entry(self):
        e = G.Entry("lex",0)
        print(f'Entry : {e.lex, e.token }')
        self.assertEqual(e.lex,'lex')
        self.assertEqual(e.token, 0)

    def test_02_add_entry_to_symbolTable(self):
        e = G.Entry("lex",0)
        G.SYMBOL_TABLE.append(e)
        print(f'SYMBOL_TABLE : {G.SYMBOL_TABLE[0].lex, G.SYMBOL_TABLE[0].token }')
        self.assertEqual(G.SYMBOL_TABLE[0].lex, 'lex')
        self.assertEqual(G.SYMBOL_TABLE[0].token, 0)

if __name__ == '__main__':
    unittest.main()