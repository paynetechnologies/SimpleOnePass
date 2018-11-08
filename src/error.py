import sys
from src.constants import constants, entry

def error(m):
    print(f'line {constants.LINE_NUMBER} : {m} ')
    sys.exit()