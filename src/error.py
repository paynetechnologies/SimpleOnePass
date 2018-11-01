import sys
import globall as G

def error(m):
    print(f'line {G.LINE_NUMBER} : {m} ')
    sys.exit()