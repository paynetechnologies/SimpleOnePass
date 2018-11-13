import sys
from src.constants import constants, entry

def error_message(ln, m):
    print(f'line {constants.line_no} : {m} ')
    sys.exit()