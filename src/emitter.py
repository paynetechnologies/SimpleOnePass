from src.constants import constants, entry

'''
def emit(t, tval):
    switcher = {
        constants.OPERATOR  : print(f'\n{t}'),
        constants.DIV       : print(f'DIV\n'),
        constants.MOD       : print(f'MOD\n'),           
        constants.NUM       : print(f'{tval}\n'),
        constants.ID        : print(f'{constants.SYMBOL_TABLE[tval].lexeme}\n'),
    }
    return switcher.get(t, f'token {t} tokenval {tval}')
'''
def emit(t, tval):
    
    # case "+": case "-": case "*": case "/":
    if (t in ['+', '-', '/', '*']):
        print(f'{t} ')

    # case DIV:        
    elif (t == constants.DIV):
        print(f'DIV ')

    # case MOD:
    elif (t == constants.MOD):
        print(f'MOD ')       

    # case NUM:
    elif (t == constants.NUM):
        print(f'{tval} ')    

    # case ID`:
    elif (t == constants.ID):
        print(f'{constants.SYMBOL_TABLE[tval].lexeme} ')     

    else:
        print(f'token {t}, tokenval {tval} ')
