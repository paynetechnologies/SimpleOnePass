import sys
import globals

def error(m):
    print(f'line {globals.LINE_NUMBER} : {m} ')
    sys.exit()