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
    
    #     case "+": case "-": case "*": case "/":
    if (t == constants.OPERATOR):
        print(f'\n{t}')
    #     case DIV:        
    elif (t == constants.DIV):
        print(f'DIV\n')
    #     case MOD:
    elif (t == constants.MOD):
        print(f'MOD\n')            
    #     case NUM:
    elif (t == constants.NUM):
        print(f'{tval}\n')            
    #     case ID`:
    elif (t == constants.ID):
        print(f'{constants.SYMBOL_TABLE[tval].lexeme}\n')            
    else:
        print(f'token {t} tokenval {tval}')


# Function to convert number into string 
# Switcher is dictionary data type here 
# def numbers_to_strings(argument): 
#     switcher = { 
#         0: "zero", 
#         1: "one", 
#         2: "two", 
#     } 
  
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    # return switcher.get(argument, "nothing")     