import sys
from src.parser import parser
from src.init import init

def main():
    init()
    p = parser( 'A + B + (C * D)' )
    p.parse()


if __name__ == '__main__':
    main()