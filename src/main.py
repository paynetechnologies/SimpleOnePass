from src.init import init_symbol_table
from src.parser import parse

def main():
    init_symbol_table()
    parse()
    exit(0)


if __name__ == '__main__':
    main()