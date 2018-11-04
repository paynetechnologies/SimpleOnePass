import sys
from src.globals import constants, entry

def error(self, m):
    print(f'line {constants.LINE_NUMBER} : {m} ')
    sys.exit()