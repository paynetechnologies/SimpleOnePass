'''                                              EndBuf       
   Start_buf                                DANGER ^  END
   ^ Next                                      ^   |   ^
   |^                                          |   |   |
   |                                           +   |   | 
   ++------------------------------------------+---+---+
   |                                           |YYY|XXX| After initial read
   |-------------------------------------------|---|---|
   |                                           |   |   |
   |                                MAXLOOK--->|   |<--|
   |<------------------ 3 x MAXLEX --------------->|   |
   |<-------------------- BUFSIZE -------------------->|
'''
'''                                              
   Start_buf                                DANGER    END
   ^                                     Next  ^       ^
   |                                       ^   | EndBuf|
   |     pmark       smark          emark  |   |   ^   | 
   +-----^-----------^--------------^------+---+---+---+
   |     |prev lexeme|current lexeme|          |YYY|XXX| Normally
   |-------------------------------------------|---|---|
   |                                                   |
   |<------------------- BUFSIZE --------------------->|
'''
'''                                              
   Start_buf                            DANGER        END
   ^                           Next       ^            ^
   |                            ^         |    EndBuf  |
   pmark    smark       emark   |         |      |     |
   ^--------^-----------^-------+---------+------+-----+
   |prev lex|current lex|       YYY            |XXXXXXX| After Flush
   |-------------------------------------------|-------|
   |                           -->| n x MAXLEX |<--    |
   |<------------------- BUFSIZE --------------------->|
'''
import io
import sys
import array
import time

class Input:

    MAXLOOK = 16        # max amount of lookahead
    MAXLEX = 1024       # max lexeme size
    BUFSIZE = (MAXLEX * 3) + (2 * MAXLOOK)      # Change the 3 only

    startBuf = [None for x in range(BUFSIZE)]   # input buffer
    startBufA = array.array('B',[0 for x in range(BUFSIZE)])

    END = startBuf[BUFSIZE - 1]                 # startBuf[BUFSIZE-1] just past last char in buf

    endBuf  = END   # just past last char
    next    = END   # next input char
    sMark   = END   # start of current lexeme
    eMark   = END   # end of current lexeme
    pMark   = END   # start of previous lexeme
    pLineno = 0     # line # of previous lexeme
    pLength = 0     # length of previous lexeme

    STDIN = sys.stdin

    inpFile     = None  # input file handle
    lineNo      = 1     # current line number
    mLine       = 1     # Line # when mark_end() is called
    termChar    = 0     # holds the char that was overwritten by \0 when last char is null terminated
    EOF_Read    = False # end of file 


# Flush buffer when next passes this address
def DANGER():
    return Input.endBuf - Input.MAXLOOK

def no_more_chars():
    return (Input.EOF_Read and Input.next >= Input.endBuf)


def ii_io(open_funct, close_funct, read_funct):
    openp = open_funct
    closep = close_funct
    readp = read_funct

def ii_newfile(self, name):

    name = input if (name == '/dev/tty') else name

    fd = Input.STDIN if name is None else open(name, mode='rb')
    print(type(fd))

    if Input.inpFile is not None and Input.inpFile != "STDIN":
        Input.inpFile.close()

    Input.inpFile = fd

    Input.EOF_Read=0
    Input.next = Input.END
    Input.sMark = Input.END
    Input.eMark = Input.END
    Input.endBuf = Input.END
    Input.lineNo = 1
    Input.mLine = 1

    return fd

def doStuff(chunk):
    lines = chunk.split(b'\n')
    for line in lines:
        print(line)

def readfile_into_buffer(filename):
    t1=0
    t2=0


    fd=open(filename,'rb',Input.BUFSIZE)
    Input.startBuf = fd.read(Input.BUFSIZE)

    start = time.time()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(Input.BUFSIZE), b''):
            doStuff(chunk)
    end = time.time()
    t1 = end-start
    
    start = time.time()
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(Input.BUFSIZE)
            if not chunk:
                break
            doStuff(chunk)
    end = time.time()
    t2 = end - start
    
    print(f't1 - {t1} : t2  {t2}')

def chunk_file(fd, chunksize=4096):
    return iter(lambda: fd.read(chunksize), b'')                

if __name__ == '__main__':
    readfile_into_buffer("./src/test_files/web.config")
