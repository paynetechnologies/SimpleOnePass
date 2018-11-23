import sys
import unittest
from src.parser import parser
from src.init import init

class Test_Main(unittest.TestCase):

    def test_01_main(self):
        print('\n\nTest_Main')
        pass
        #init()
        p = parser( 'A + B' )
        #p = parser( 'A + B + (C * D)' )
        #p = parser( '(A * B) + (C * D)' )
        #p = parser( '(E + F) * (G + H)' )
        #p.parse()



if __name__ == '__main__':
    unittest.main()