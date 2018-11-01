import unittest
import universal as U

class TestLexer(unittest.TestCase):
    """ Test lexer variables """
    
    def test_01_create_entry(self):
        e = U.Entry("lexptr",0)
        print(f'Entry : {e.lexptr, e.token }')
        self.assertEqual(e.lexptr,'lexptr')
        self.assertEqual(e.token, 0)

    def test_02_add_entry_to_symbolTable(self):
        e = U.Entry("lexptr",0)
        U.Symbol_Table.append(e)
        print(f'Symbol_Table : {U.Symbol_Table[0].lexptr, U.Symbol_Table[0].token }')
        self.assertEqual(U.Symbol_Table[0].lexptr, 'lexptr')
        self.assertEqual(U.Symbol_Table[0].token, 0)

if __name__ == '__main__':
    unittest.main()