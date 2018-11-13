import sys
from src.parser import parser
from src.init import initialize

def main():
    #initialize()
    p = parser('abc + 5')
    #p = parser('9+5')
    #p = parser('9 + 5 - 2')
    #p = parser(';')
    p.parse()


if __name__ == '__main__':
    main()