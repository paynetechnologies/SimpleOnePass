import unittest
from src.token import Token
from src.symbol_table import entry

class Test_Entry(unittest.TestCase):
    """ Test Symbol_Table variables """

    def setUp(self):
        print('\n\nTest_Entry')
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    def test_01_create_entry(self):
        self.e1 = entry(token=Token.ID, value="Identifier")
        self.assertEqual(self.e1.lexeme,'Identifier')
        self.assertEqual(self.e1.token, Token.ID)

if __name__ == '__main__':
    unittest.main()

