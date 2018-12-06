from src.symbol_table import SymbolTable, Entry
from src.token import Token

'''
def emit(t, tval):
    switcher = {
        Token.OPERATOR  : print(f'\n{t}'),
        Token.DIV       : print(f'DIV\n'),
        Token.MOD       : print(f'MOD\n'),           
        Token.NUM       : print(f'{tval}\n'),
        Token.ID        : print(f'{Token.symbol_table[tval].lexeme}\n'),
    }
    return switcher.get(t, f'token {t} tokenval {tval}')
'''
def emit(t, tval):
    print(f'emit t : {t} - tval : {tval}')
    # case "+": case "-": case "*": case "/":
    if (t in ['+', '-', '/', '*']):
        print(f'{t} ')

    # case DIV:        
    elif (t == Token.DIV):
        print(f'DIV ')

    # case MOD:
    elif (t == Token.MOD):
        print(f'MOD ')       

    # case NUM:
    elif (t == Token.NUM):
        print(f'{tval} ')    

    # case ID`:
    elif (t == Token.ID):
        print(f'{SymbolTable.symbol_table[tval].lexeme} ')     

    else:
        print(f'token {t}, tokenval {tval} ')
