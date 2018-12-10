'''                                               EndBuf       
   Start_buf                                DANGER  |  END
   | Next                                      |    |   |
   |/                                          |    |   |
   v                                           v    v   v 
   +-------------------------------------------+---+---+
   |                                           |YYY|XXX| After initial read
   |-------------------------------------------|---|---|
   |                                           |   |   |
   |                                MAXLOOK--->|   |<--|
   |<------------------ 3 x MAXLEX --------------->|   |
   |<-------------------- BUFSIZE -------------------->|
'''
'''                                              
   Start_buf                       Next      DANGER    END
   |     pmark    smark        emark |         |  EndBuf|
   |     |        |            |     |         |    |   |
   v     v        v            v     v         v    v   v 
   +-------------------------------------------+---+---+
   |     |prev lex|current lex|                |YYY|XXX| Normally
   |-------------------------------------------|---|---|
   |                                                   |
   |<------------------- BUFSIZE --------------------->|
'''
'''                                              
   Start_buf                            DANGER          END
   |                           Next       |   EndBuf    |
   v                            |         |     |       |
   pmark    smark       emark   |         |     v       v
   v--------v-----------v-------v---------v-------------
   |prev lex|current lex|      |YYY|           |XXXXXXX| After Flush
   |-------------------------------------------|-------|
   |                           -->| n x MAXLEX |<--    |
   |<------------------- BUFSIZE --------------------->|
'''
import io
import sys
import array
import time



class Input:

    EOF     = False
    MAXLOOK = 16        # max amount of lookahead
    MAXLEX  = 1024      # max lexeme size
    BUFSIZE = (MAXLEX * 3) + (2 * MAXLOOK)      # Change the 3 only

    StartBuf = array.array('B', [0 for x in range(BUFSIZE)])

    END = BUFSIZE   # just past last char in buf

    endBuf  = END   # just past last char
    Next    = END   # Next input char
    sMark   = END   # start of current lexeme
    eMark   = END   # end of current lexeme
    pMark   = END   # start of previous lexeme
    pLineno = 0     # line # of previous lexeme
    pLength = 0     # length of previous lexeme

    STDIN = sys.stdin # default standard input

    inpFile     = STDIN  # input file handle
    Lineno      = 1     # current line number
    Mline       = 1     # Line # when mark_end() is called
    Termchar    = 0     # holds the char that was overwritten by \0 when last char is null terminated
    EOF_Read    = False # end of file 

    ii_io = {}

    been_called = False

#---------------------------------------------------
#                      I/O
#---------------------------------------------------
def open_funct(filename, mode):
    fd=open(filename,mode)
    return fd

def close_funct(fd):
    fd.close()

def read_funct(fd, starting_at, need):
    #Input.StartBuf = fd.read(Input.BUFSIZE)
    bytesToRead = fd.seek(need, starting_at)
    #Input.StartBuf = fd.read(bytesToRead)
    Input.StartBuf.fromfile(Input.inpFile, bytesToRead)
    print(Input.StartBuf)
    return bytesToRead

def ii_io(open_funct, close_funct, read_funct):
    Input.ii_io["openp"] = open_funct
    Input.ii_io["closep"]= close_funct            
    Input.ii_io["readp"] = read_funct
    print(Input.ii_io)


#---------------------------------------------------
#                      Access
#---------------------------------------------------

def ii_text():
    return Input.sMark

def ii_length():
    return Input.eMark - Input.sMark

def ii_lineno():
    return Input.Lineno

def ii_ptext():
    return Input.pMark

def ii_plength():
    return Input.pLength

def ii_plineno():
    return Input.pLineno

def ll_mark_start():
    Input.Mline = Input.Lineno
    Input.eMark = Input.sMark = Input.Next
    return Input.sMark

def ii_mark_end():
    Input.Mline = Input.Lineno
    Input.eMark = Input.Next
    return Input.eMark

def ii_mark_start():
    if (Input.sMark >= Input.eMark):
        return None
    else:
        return ++Input.sMark

def ii_to_mark():
    Input.Lineno = Input.Mline
    Input.Next = Input.eMark
    return Input.Next

def ii_mark_prev():
    '''
    Set the pMark. Note: a buffer flush won't go past pMark so
    once you save it, you must move it every time you move sMark.
    This is not done automatically, since you may want to 
    remember the token before last rather than the last one.
    If ii_pmark_prev is never called, pMark is ignored, no worries;
    '''

    Input.pMark = Input.sMark
    Input.pLineno = Input.Lineno
    Input.pLength = Input.eMark - Input.sMark
    return Input.pMark

# Flush buffer when Next passes this address
def DANGER():
    return Input.endBuf - Input.MAXLOOK

def NO_MORE_CHARS():
    return (Input.EOF_Read and Input.Next >= Input.endBuf)

#---------------------------------------------------
#                      Open Read File
#---------------------------------------------------
def ii_newfile(name=None):
    '''
    Prepare a new iput file for reading. If newfile() isn't called before
    input() or input_line() then stdin is used. The current input file is
    closed after successfully opening the new one (but stdin is not closed.)
    
    Return -1 if the file can't be opened, otherwise, return the file
    descripotor returned from open(). Note: the old input file won't be 
    closed unless the new file is opened successfully The error code (errno)
    generated by the bad open() will still be valid, so you can call perror()
    to find out what went wrong if you like. At least one free file
    descriptor must be available when newfile() is called. Note in the open
    call that 'rb' is used to open read in binary mode.
    '''

    fd = None # file descriptor

    name = input if (name == '/dev/tty') else name

    fd = Input.STDIN if name is None else Input.ii_io["openp"](name, 'rb')

    if(fd != 0):   
        print(type(fd))

        if Input.inpFile != Input.STDIN:
            Input.ii_io["closep"](Input.inpFile)

        Input.inpFile = fd
        Input.EOF_Read = False

        Input.Next      = Input.END
        Input.sMark     = Input.END
        Input.eMark     = Input.END
        Input.endBuf    = Input.END
        Input.Lineno    = 1
        Input.Mline     = 1

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

#---------------------------------------------------
#                      Advance Flush Fill 
#---------------------------------------------------
def ii_advance():
    '''
    ii_advance is the real input function. It returns the Next character
    from input and advances past it. The buffer is flushed if the current
    character is within MAXLOOK characters of the end of the buffer. 0 is
    returned at the end of file. -1 returned if the buffer can't be flushed
    because it's too full. In this case, you can call ii_flush(1) to do a
    buffer flush but you'll lose the curent lexeme as a result.
    '''
    if (not Input.been_called):
        # push a newline on the empty buffer so LEX start-of-line
        # will work on the first input line.
        Input.Next = Input.sMark = Input.eMark = Input.END - 1
        Input.StartBuf.insert(Input.Next, '\n')
        Input.Lineno -= 1
        Input.Mline -= 1
        Input.been_called = True

    if (NO_MORE_CHARS()):
        return 0

    if (not Input.EOF_Read and (ii_flush(0) < 0)):
        return -1

    if (Input.Next == '\n'):
        Input.Lineno += 1

    Input.Next +=1
    return (Input.StartBuf[Input.Next])

def ii_flush(force):
    '''
    Flush the input buffer. Do nothing if the current input characters isn't
    in the danger zone, otherwise move all unread characters to the left end
    of the buffer and fill the remainder of the buffer. Note that input()
    flushes the buffer willy-nilly if you read past the end of buffer.
    Similarly, input_line() flushes the buffer at the beginning of each line.
                                      
   Start_buf                       Next      DANGER    END
   |        pmark smark        emark |         |  EndBuf|
   |        |     |            |     |         |    |   |
   v        v     v            v     v         v    v   v 
   +-------------------------------------------+---+---+
   | this is already read | to be read Next    | waste |
   |-------------------------------------------|-------|
   |<------ shift_amt --->|<----copy_amt------>|       |
   |                                                   |
   |<------------------- BUFSIZE --------------------->|

    Either the pMark of sMark, whichever is smaller, is used as the leftmost
    edge of the buffer. None of the text to the right of the mark will be 
    lost. Return 1 if OK, -1 if buffer is full and can't be flushed, 0 if 
    at end-of-file. If force is true, a buffer flush is forced and the 
    characters already in it are discarded. Don't call this function on a 
    buffer that's been terminated by ii_term()
    '''
    copy_amt = shift_amt = left_edge = 0

    if (NO_MORE_CHARS()):
        return 0

    if (Input.EOF_Read):    # nothing more to read
        return 1

    if (Input.Next >= DANGER() or force):

        left_edge = min(Input.sMark, Input.pMark) if Input.pMark else Input.sMark
        shift_amt = left_edge - Input.StartBuf

        if (shift_amt < Input.MAXLEX): # if not enough room 
            if (not force):
                return -1

            left_edge = ii_mark_start() # reset start to current character
            ii_mark_prev()
            shift_amt = left_edge - Input.StartBuf

        copy_amt = Input.endBuf - left_edge

        copy(Input.StartBuf, left_edge, copy_amt)

        if (not ii_fillBuf(Input.StartBuf + copy_amt)):
            #ferr("INTERNAL ERROR, ii_flush: Buffer full, can't read \n")
            pass
        
        if (Input.pMark):
            Input.pMark -= shift_amt

        Input.sMark = shift_amt
        Input.eMark = shift_amt
        Input.Next = shift_amt

    return 1

def ii_fillBuf(starting_at):
    '''
    Fill the input buffer from starting_at to the end of the buffer.
    The input file is not closed when EOF is reached. Buffers are read
    in units of MAXLEX characters; it's an error if that any characters
    cannot be read (0 is returned in this case). For example, if MAXLEX
    is 1024, then 1024 characters will be read at a time. The number of
    characters read is returned. Eof_read is true as soon as the last
    buffer is read.

    PORTABILITY NOTE: I'm assuming that the read function actually returns
    the number of characters loaded into the buffer, and that that number 
    will be < need only when the last chunk of the file is read. It's 
    possible for read() to always return fewer than the number of requested 
    characters in MS-DOS untranslated-input mode, however (if the File is opened 
    without the O_BINARY flag). That's not a problem hhere because the file is 
    opened in binary mode, but it could cause problems if you change from binary 
    to text mode at some point.
    '''
    need = 0 # number of bytes needed from input
    got = 0  # number of bytes actually read

    need = int((( Input.END  - starting_at) / Input.MAXLEX) * Input.MAXLEX)

    print(f'Reading {need} bytes \n')

    if (need < 0):
        #ferr("INTERNAL ERROR (ii_filBuf( : Bad rea-request starting addr. \n")
        pass

    if (need == 0):
        return 0

    got = Input.ii_io["readp"](Input.inpFile, starting_at, need)
    if (got == None):
        pass
        print(f"Can't read input file. \n")
        return -1

    Input.endBuf = starting_at + got

    if (got < need):
        Input.EOF_Read = True

    return got
        
#---------------------------------------------------
#                      Copy Shift
#---------------------------------------------------
def copy(buf, left, amt):
    for i in range(amt):
        shiftContentsLeft(buf, left)
  
# Function to left Rotate arr[] of size n by 1*/  
def shiftContentsLeft(arr, n): 
    temp = arr[0] 
    for i in range(n-1): 
        arr[i] = arr[i + 1] 
    arr[n-1] = temp 

#---------------------------------------------------
#                      LookAhead PushBack
#---------------------------------------------------
def ii_look(n):
    '''
    Return the nth character of lookahead, EOF if you try to look past
    end of file, or 0 if you try to look past either end of the buffer.
    '''
    p = None
    p = Input.Next + (n - 1)

    if (not Input.EOF_Read and p >= Input.endBuf):
        Input.EOF = True
        return Input.EOF

    return 0 if (p < Input.StartBuf or p >= Input.endBuf) else Input.StartBuf[p]

def ii_pushback(n):
    '''
    Push n characters back into the input. You can't push past the current
    sMark. You can, however, push back characters after end of file has
    been encountered.
    '''
    n -= 1
    while ( n >= 0 and Input.Next > Input.sMark):
        
        if( Input.StartBuf[Input.Next] == '\n' or Input.Next == 0):
            Input.Lineno -= 1

        if (Input.Next < Input.eMark):
            Input.eMark =  Input.Next
            Input.Mline = Input.Lineno

        n -= 1

    return( Input.Next > Input.sMark )    

#---------------------------------------------------
#                      Terminate Unterminate
#---------------------------------------------------
def ii_term():
    Input.Termchar = Input.StartBuf[Input.Next]
    Input.StartBuf[Input.Next] = '\0'

def ii_unterm():
    if( Input.Termchar):
        Input.StartBuf[Input.Next] = Input.Termchar;
        Input.Termchar = 0

def ii_input():
    rval = None
    
    if(Input.Termchar):
        ii_unterm()
        rval = ii_advance()
        ii_mark_end()
        ii_term()
    else:
        rval = ii_advance()
        ii_mark_end ()
    return rval

def ii_unput(c):

    if(Input.Termchar):
        ii_unterm()
        if( ii_pushback(1) ):
            Input.StartBuf[Input.Next] = c
            ii_term()
    else:
        if( ii_pushback(1)):
            Input.StartBuf[Input.Next] = c

def ii_lookahead( n ):
    return Input.Termchar if (n == 1 and Input.Termchar is not None) else ii_look(n)

def ii_flushbuf():
    if (Input.Termchar is not None):    
        ii_unterm()
    return ii_flush(1)



#################################################
# Python3 program to rotate an array by  
# d elements  
# Function to left rotate arr[] of size n by d*/ 
def leftRotate(arr, d, n): 
    for i in range(d): 
        leftRotatebyOne(arr, n) 
  
# Function to left Rotate arr[] of size n by 1*/  
def leftRotatebyOne(arr, n): 
    temp = arr[0] 
    for i in range(n-1): 
        arr[i] = arr[i + 1] 
    arr[n-1] = temp 
          
# utility function to print an array */ 
def printArray(arr, size): 
    for i in range(size): 
        print ("% d"% arr[i], end =" ") 
  

  

if __name__ == '__main__':
    #readfile_into_buffer("./test_files/web.config") #python input.py
    #readfile_into_buffer("./src/test_files/web.config") #DEBUG
    
    ii_io(open_funct, close_funct, read_funct)
    ii_newfile('./src/test_files/web.config') 
    ii_fillBuf(0)
    ii_advance()

    # Driver program to test above functions */ 
    # arr = array.array('B', [x for x in range(10)])
    # #arr = [1, 2, 3, 4, 5, 6, 7] 
    # leftRotate(arr, 2, 7) 
    # printArray(arr, 7) 
