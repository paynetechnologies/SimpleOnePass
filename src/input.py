import io
import sys

MAXLOOK = 16        # max amount of lookahead
MAXLEX = 1024       # max lexeme size
BUFSIZE = (MAXLEX * 3) + (2 * MAXLOOK)

startBuf = [None for x in range(BUFSIZE)]   # input buffer
END = BUFSIZE - 1 # startBuf[BUFSIZE-1]     # just past last char in buf

endBuf = END    # just past last char
next = END      # next input char
sMark = END     # start of current lexeme
eMark = END     # end of current lexeme
pMark = END     # start of previous lexeme
pLineno = 0     # line # of previous lexeme
pLength = 0     # length of previous lexeme

STDIN = sys.stdin

inpFile = None # input file handle
lineNo = 1      # current line number
mLine = 1       # Line # when mark_end() is called
termChar = 0    # holds the char that was overwritten by \0 when last char is null terminated
EOF_Read = False # end of file 


# Flush buffer when next passes this address
def DANGER():
    return endBuf - MAXLOOK

def no_more_chars():
    return (EOF_Read and next >= endBuf)


def ii_io(open_funct, close_funct, read_funct):
    openp = open_funct
    closep = close_funct
    readp = read_funct

def ii_newfile(name):

    fd=''

    name = input if (name == '/dev/tty') else name

    fd = STDIN if name is None else open(name, mode='rb')
    print(type(fd))

    if inpFile is not None and inpFile != "STDIN":
        inpFile.close()

    inpFile = fd

    EOF_Read=0
    next = END
    sMark = END
    eMark = END
    endBuf = END
    lineNo = 1
    mLine = 1

    return fd



if __name__ == '__main__':
    ii_newfile(None)
