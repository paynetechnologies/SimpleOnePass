import sys
import universal as U

inputString = "9+5-2@" 
lookahead = ""
ptr = 0
EOF = False



lexbuf = [None] * BSIZE
line_nbr = 1
token_value = None

def getchar():
    global ptr

    c = inputString[ptr]
    if (c == '@'):
        EOF = True
    ptr += 1
    return c

class lexman():
    t=''

    while(True):
        t = getchar()