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


def open_funct(filename, mode):
    fd=open(filename,mode)
    return fd

def close_funct(fd):
    fd.close()

def read_funct(fd):
    Input.startBuf = fd.read(Input.BUFSIZE)
    

class Input:

    MAXLOOK = 16        # max amount of lookahead
    MAXLEX = 1024       # max lexeme size
    BUFSIZE = (MAXLEX * 3) + (2 * MAXLOOK)      # Change the 3 only

    #startBuf = [None for x in range(BUFSIZE)]   # input buffer
    startBuf = array.array('B', [0 for x in range(BUFSIZE)])

    END = BUFSIZE - 1  # startBuf[BUFSIZE-1] just past last char in buf

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

    ii_io = {}


def ii_io(open_funct, close_funct, read_funct):
    Input.ii_io["openp"] = open_funct
    Input.ii_io["closep"]= close_funct            
    Input.ii_io["readp"] = read_funct
    print(Input.ii_io)


# Flush buffer when next passes this address
def DANGER():
    return Input.endBuf - Input.MAXLOOK


def no_more_chars():
    return (Input.EOF_Read and Input.next >= Input.endBuf)


def ii_newfile(name=None):

    ii_io(open_funct, close_funct, read_funct)

    fd=None

    name = input if (name == '/dev/tty') else name

    #fd = Input.STDIN if name is None else open(name, mode='rb')
    fd = Input.STDIN if name is None else Input.ii_io["openp"](name, 'rb')
    if(fd != 0):   
        print(type(fd))

        if Input.inpFile is not None and Input.inpFile != "STDIN":
            Input.ii_io["closep"](Input.inpFile)

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
    #t2=0

    ii_io(open_funct, close_funct, read_funct)

    Input.ii_io["openp"](filename, 'rb')
    #fd=open(filename,'rb',Input.BUFSIZE)
    #Input.startBuf = fd.read(Input.BUFSIZE)

    start = time.time()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(Input.BUFSIZE), b''):
            doStuff(chunk)
    end = time.time()
    t1 = end-start
    print(f't1 - {t1}')
    '''
    start = time.time()
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(Input.BUFSIZE)
            if not chunk:
                break
            doStuff(chunk)
    end = time.time()
    t2 = end - start
    '''
    
    #print(f't1 - {t1} : t2  {t2}')

def chunk_file(fd, chunksize=Input.BUFSIZE):
    return iter(lambda: fd.read(chunksize), b'')                

if __name__ == '__main__':
    #readfile_into_buffer("./test_files/web.config") #python input.py
    #readfile_into_buffer("./src/test_files/web.config") #DEBUG
    ii_newfile('./src/test_files/web.config') 
