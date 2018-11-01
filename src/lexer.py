import sys
import error
import globall as G

G.LINE_NUMBER = 1
G.token_value = None

inputString = "9+5-2;" 
lookahead = ""
ptr = 0
EOF = False
lexbuf = [None] * G.BSIZE


def getchar():
    global ptr

    c = inputString[ptr]
    if (c == ';'):
        G.EOF = True
    ptr += 1
    return c

def ungetchar(c):
    global ptr
    ptr -= 1

def isNewLine(t):
    if (t == "\n"):
        return True
    return False

def isWhiteSpace(t):
    if (t == "" or t =="\t"):
        return True
    return False

class lexman():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def lex(self):
        t=""
        while(True):
            t = getchar()

            if (isWhiteSpace(t)):
                pass

            elif (isNewLine(t)):
                G.LINE_NUMBER += 1

            elif (t.isdigit(t)):
                ungetchar(t)
                print(f't : {t}')
                return G.NUM

            elif (t.isalpha):
                p = b = 0
                while (t.isalnum):
                    lexbuf[b] = t
                    t = getchar()
                    b += 1
                    if (b >= G.BSIZE):
                        pass
                        # error("compiler error")

                lexbuf[b] = G.EOS

                if (t != EOF):
                    ungetchar(t)
                
                # p = lookup(lexbuf)
                
                # if (p == 0):
                #     p = insert(lexbuf, ID)
                # G.TOKEN_VALUE = p
                
                # return SYMBOL_TABLE[p].token
            
            elif (t == EOF):
                return G.DONE

            else:
                G.TOKEN_VALUE = G.NONE
                return t
