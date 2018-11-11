import sys
from src.parser import parser
from src.init import initialize

def main():
    #initialize()
    p = parser('9 + 5 - 2 ;')
    p.parse()


if __name__ == '__main__':
    main()