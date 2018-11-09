from src.init import initialize
from .parser import parser


def main():
    #initialize()
    parser('9 + 5 - 2 ;')
    exit(0)


if __name__ == '__main__':
    main()