
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
   Start_buf                            DANGER         END
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
import string


class Input:
    BINARY = True

    MAXLOOK = 16                                # max amount of lookahead
    MAXLEX  = 1024                              # max lexeme size
    BUFSIZE = (MAXLEX * 3) + (2 * MAXLOOK)      # Change the 3 only
    # str
    #StartBuf = [0 for x in range(BUFSIZE)]      # StartBuf = ['' for x in range(BUFSIZE)]
    # array
    StartBuf = array.array('B', [96 for x in range(BUFSIZE)]) # StartBuf = ['' for x in range(BUFSIZE)]
    MVStartBuf = memoryview(StartBuf)
    END = BUFSIZE                               # just past last char in buf

    EndBuf  = END   # logical buffer end...just past last char
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

    been_called = True
    EOF         = True  # constant
    EOF_Read    = False 
    ''' 
    End of file has been read. It's possible for this to be true 
    and for characters to still be in the input buffer.
    '''

    ii_io = {}                                  # pointers to Open, Read, Close functions

    whitespace = ' \r\t\n'
    newline = '\n'
    comment_marker = ['<!-']

#---------------------------------------------------
#                      I/O
#---------------------------------------------------
# Flush buffer when Next passes this address
def DANGER():
   return Input.EndBuf - Input.MAXLOOK

def NO_MORE_CHARS():
    if (Input.EOF_Read and Input.Next >= Input.EndBuf):
        return 

def open_funct(filename, mode, encoding=None):
    fd=open(filename, mode, encoding=encoding)
    return fd

def close_funct(fd):
    fd.close()

def read_funct(fd, starting_at, need):
    #fd.seek(starting_at, 1)

    if Input.BINARY == False:
        print(f'Input.StartBuf : {Input.StartBuf}')

    begin_seek_pos = fd.tell()
    try:
        # str
        #Input.StartBuf = fd.read(need)
        # if using array.array
        ##Input.StartBuf.fromfile(fd, need)
        Input.MVStartBuf = fd.read(need)

    except EOFError:
        Input.EOF_Read = True
    except Exception as e :
        print(f"Unexpected error : {e}", sys.exc_info()[0])
        raise
    
    got = min(fd.tell() - begin_seek_pos, need)
    
    if Input.BINARY:
        #print(f'{[chr(c) for c in Input.StartBuf]}')
        #print(''.join([chr(c) for c in Input.StartBuf]))
        print(''.join([chr(c) for c in Input.MVStartBuf]))
    else:
        print(f'{c for c in Input.StartBuf}')

    return got

def ii_io(open_funct, close_funct, read_funct):
    '''
    Used to change the low-level input functions that
    are used to open files and fill the buffer.
    '''
    Input.ii_io["openp"] = open_funct
    Input.ii_io["closep"]= close_funct            
    Input.ii_io["readp"] = read_funct
    print(Input.ii_io)


#---------------------------------------------------
#                      Access
#---------------------------------------------------
def ii_text():
    '''Pointer to current lexeme'''
    return Input.sMark

def ii_length():
    ''' lexeme length'''
    return Input.eMark - Input.sMark

def ii_lineno():
    '''line number of last char in lexeme'''
    return Input.Lineno

def ii_ptext():
    '''Pointer to previous lexeme'''
    return Input.pMark

def ii_plength():
    '''previous lexeme length'''
    return Input.pLength

def ii_plineno():
    '''line number of last char in previsous lexeme'''
    return Input.pLineno

def ii_mark_start():
    '''
    Moves the sMark to the current input position (pointed to by Next). 
    It also makes sure that the end-of-lexeme marker (eMark) is not to 
    the left of the start marker.
    '''
    Input.Mline = Input.Lineno
    Input.eMark = Input.sMark = Input.Next
    return Input.sMark

def ii_mark_end():
    '''
    Similar to ii_mark_start...
    It also saves the current line number in Mline, because the lexical analyzer 
    might sweep past a newline when it scans forward looking for a new lexeme. 
    The input line number must be restored to the condition it was in before the 
    extra newline was scanned when the analyzer returns to the previous end marker
    '''
    Input.Mline = Input.Lineno
    Input.eMark = Input.Next
    return Input.eMark

def ii_move_start():
    '''
    Move the start marker one space to the right. 
    It returns the new start marker on success, NULL if you tried to move past 
    the end marker (sMark is not modified in this last case). 
    '''
    if (Input.sMark >= Input.eMark):  
        return None  
    else: 
        Input.sMark += 1
        return Input.sMark

def ii_to_mark():
    '''
    Restores the input pointer to the last end mark
    '''
    Input.Lineno = Input.Mline
    Input.Next = Input.eMark
    return Input.Next

def ii_mark_prev():
    '''
    Modifies the previous-lexeme marker to reference the same lexeme as the 
    current-lexeme marker. Typically, ii_mark_prev() is called by the lexical
    analyzer just before calling ii_mark_start() (that is, just before it begins 
    to search for the next lexeme ).
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


#---------------------------------------------------
#                      Open Read File
# The normal mechanism for opening a new input file. 
# It is passed the file name and returns the file descriptor (not the
# FILE pointer) for the opened file, or -1 if the file couldn't be opened. 
# The previous input file is closed unless it was standard input. 
# ii _new fi1e() does not actually read the first buffer; rather, it 
# sets up the various pointers so that the buffer is loaded the first time a 
# character is requested. This way, programs that never call ii_newfile() will
# work successfully, getting input from standard input. The problem with this approach is
# that you must read at least one character before you can look ahead in the input (otherwise
# the buffer won't be initialized). If you need to look ahead before advancing, use:
#     ii_advance(); Read first bufferfull of input 
#     ii_pushback(l); but put back the first character 
# The default input stream [used if ii newfile() is never called] is standard input.
# You can reassign the input to standard input (say, after you get input from a file) 
# by calling: ii_newfile(NULL)
#
# Note that the input buffer is not read by ii newfile ( ) ; rather, the various pointers
# are initialized to point at the end of the buffer. The actual input routine (advance (), 
# discussed below) treats this situation the same as it would the Next pointer crossing 
# the DANGER point. It shifts the buffer's tail all the way to the left (in this case 
# the tail is empty so no characters are shifted, but the pointers are moved), and then loads the buffer 
# from the disk.
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

    if Input.BINARY:
        fd = Input.STDIN if name is None else Input.ii_io["openp"](name, 'rb', )
    else:
        fd = Input.STDIN if name is None else Input.ii_io["openp"](name, 'r', 'utf-8')
       
    '''
    Note that the indirect open () call uses the 'rb' BINARY input mode. A CR-LF
    (carriage-return, linefeed) pair is not translated into a single '\n' when binary-mode
    input is active. This behavior is desirable in most LEX applications, which treat both CR
    and LF as white space. There's no point wasting time doing the translation. The lack of
    translation might cause problems if you're looking for an explicit '\n' in the input,
    though.
    '''


    if(fd != 0):   
        print(type(fd))

        if Input.inpFile != Input.STDIN:
            Input.ii_io["closep"](Input.inpFile)

        Input.inpFile = fd
        Input.EOF_Read = False

        Input.Next      = Input.END
        Input.sMark     = Input.END
        Input.eMark     = Input.END
        Input.EndBuf    = Input.END
        Input.Lineno    = 1
        Input.Mline     = 1

    return fd

def doStuff(chunk):
    lines = chunk.split(b'\n')
    for line in lines:
        print(line)


    #readfile_into_buffer("./test_files/web.config") #python input.py
    #readfile_into_buffer("./src/test_files/web.config") #DEBUG

def readfile_into_buffer(filename):
    t1=0
    #t2=0

    ii_io(open_funct, close_funct, read_funct)

    Input.ii_io["openp"](filename, 'r')

    start = time.time()

    with open(filename, 'r') as f:
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

def Need_Extra_newLine():     

        '''
        Push a newline on the empty buffer so LEX start-of-line
        will work on the first input line.
        Provided for those situations where you want an extra newline appended 
        to the beginning of a file. LEX needs this capability for processing the 
        start-of-line anchor-a mechanism for recognizing strings only if they appear 
        at the far left of a line. Such strings must be preceded by a newline, so an 
        extra newline has to be appended in front of the first line of the file; otherwise, 
        the anchored expression wouldn't be recognized on the first line.4
        '''
        Input.Next = Input.sMark = Input.eMark = Input.END - 1
        
        # str
        # does this add to next or end of buffer
        # Input.StartBuf[Input.Next] + '*' #\n'
        
        # byte array 
        # *Next = '\n'
        # Input.membuf[Input.Next] = '\n'
        Input.StartBuf.insert(Input.Next, ord('\n'))

        Input.Lineno -= 1
        Input.Mline -= 1
        Input.been_called = True

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
        Need_Extra_newLine()

    if (NO_MORE_CHARS()):
        return 0

    if (not Input.EOF_Read and (ii_flush(0) < 0)):
        return -1

    #if (Input.StartBuf[Input.Next] == ord('\n')):
    if (Input.MVStartBuf[Input.Next] == ord('\n')):        
        # if *Next = '\n' or Input.membuf[Input.Next] = '\n'
        Input.Lineno += 1

    #c = Input.StartBuf[Input.Next]
    c = Input.MVStartBuf[Input.Next]

    Input.Next +=1
    return (c)


def ii_flush(force):
    '''
    Flush the input buffer. Do nothing if the current input characters isn't
    in the danger zone, otherwise move all unread characters to the left end
    of the buffer and fill the remainder of the buffer. Note that input()
    flushes the buffer willy-nilly if you read past the end of buffer.
    Similarly, input_line() flushes the buffer at the beginning of each line.
                                      
   Start_buf    pmark              DANGER              END
   |            |smark        emark  |Next        EndBuf|
   |            | |            |     | |            |   |
   v            v v            v     v v            v   v 
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
    copy_amt = shift_amt = 0
    left_edge = None

    if (NO_MORE_CHARS()):
        return 0

    if (Input.EOF_Read):    # nothing more to read
        return 1

    if (Input.Next >= DANGER() or force):        

        left_edge = min(Input.sMark, Input.pMark) if Input.pMark > 0 else Input.sMark
        
        shift_amt = left_edge - 0 # if using pointers: shift_amt = left_edge - Input.StartBuf

        #---------------------------------------------------
        # Test to see that there will be enough room after the move to load a new 
        # MAXLEX-sized bufferfull of characters. There might not be if the buffer contains
        # two abnormally long lexemes. The test evaluates true if there isn't enough room.
        # Normally, the routine returns -1 if there's no room, and 1 is returned if everything is
        # okay. 
        #
        # If the force argument is true, however, the buffer is flushed even if there's no
        # room, and 1 is returned. 
        #
        # The flush is forced by setting the start marker to the current
        # input position and the left_edge of the character to be shifted to the Next pointer,
        # effectively destroying the current lexeme.
        #---------------------------------------------------

        if (shift_amt < Input.MAXLEX): # if not enough room 
            if (not force):
                return -1

            left_edge = ii_mark_start() # reset start to current character
            ii_mark_prev()
            shift_amt = left_edge - 1 # if using pointers: shift_amt = left_edge - Input.StartBuf

        # How many characters have to be copied (copy_ amt) 
        # and the distance that they have to be moved (shift_amt).
        copy_amt = Input.EndBuf - left_edge

        copy(Input.MVStartBuf, left_edge, copy_amt)

        #if (not ii_fillBuf(Input.StartBuf + copy_amt)): # if using pointers: Input.StartBuf is 1
        if (not ii_fillBuf(copy_amt)): 
            print(f"????? INTERNAL ERROR, ii_flush: Buffer full, can't read \n")
        
        if (Input.pMark > 0):
            Input.pMark -= shift_amt

        Input.sMark -= shift_amt
        Input.eMark -= shift_amt
        Input.Next -= shift_amt

    return 1

#--------------------------------------------
# Pass a base address, and load as many MAXLEX-sized chunks into the buffur as will fit. 
# The need variable is the amount needed. The logical-end-of-buffer marker is adjusted 
# Note that a single read() call does the actual read. (Readp is initialized to point 
# at read () when it is declared up at the top of the file.) 
# This can cause problems when a lexeme can span a line, and input is fetched
# from a line-buffered input device (such as the console). 
# You'll have to use ii_io() to supply an alternate read function, in this case.
#---------------------------------------------
def ii_fillBuf(starting_at):
    '''
    Fill the input buffer from starting_at to the end of the buffer.
    The input file is not closed when EOF is reached. Buffers are read
    in units of MAXLEX characters; it's an error if that any characters
    cannot be read (0 is returned in this case). For example, if MAXLEX
    is 1024, then 1024 characters will be read at a time. The number of
    characters read is returned. Eof_read is true as soon as the last
    buffer is read.

    PORTABILITY NOTE: assuming that the read function actually returns
    the number of characters loaded into the buffer, and that that number 
    will be < need only when the last chunk of the file is read. It's 
    possible for read() to always return fewer than the number of requested 
    characters in MS-DOS untranslated-input mode, however (if the File is opened 
    without the O_BINARY flag). That's not a problem here because the file is 
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

    # do the read
    got = Input.ii_io["readp"](Input.inpFile, starting_at, need)

    if (got == None):
        pass
        print(f"Can't read input file. \n")
        return -1

    Input.EndBuf = starting_at + got

    if (got < need):
        Input.EOF_Read = True

    return got
        
#---------------------------------------------------
#                      Copy Shift
#---------------------------------------------------
def copy(buf, left, amt):
    for i in range(amt):
        shiftContentsLeft(buf, left)
    printArray(buf,amt)
  
# Function to left Rotate arr[] of size n by 1*/  
def shiftContentsLeft(arr, n): 
    #temp = arr[0] 
    for i in range(n-1): 
        arr[i] = arr[i + 1] 
    #arr[n-1] = temp 

    

#---------------------------------------------------
#                      LookAhead PushBack
# Returns the character at Lookahead, the offset from the current character that's 
# specified in its argument. An ii_look(0) returns the character that was returned 
# by the most recent ii_advance() call, ii_look(l) is the following character, 
# ii_look(-1) is the character that precedes the current one. 
# MAXLOOK characters of lookahead are guaranteed, though fewer might be available 
# if you're close to end of file; Similarly, lookback (with a negative offset) is
# only guaranteed as far as the start of the buffer (the pMark or sMark, whichever is
# smaller). Zero is returned if you try to look past end or start of the buffer, EOF if you try
# to look past end of file.
#---------------------------------------------------
def ii_look(n):
    '''
    Return the nth character of lookahead, EOF if you try to look past
    end of file, or 0 if you try to look past either end of the buffer.
    '''
    p = None
    p = Input.Next + (n - 1)

    if (Input.EOF_Read and p >= Input.EndBuf):
        return Input.EOF

    return 0 if (p < Input.StartBuf or p >= Input.EndBuf) else Input.StartBuf[p]

#------------------------------------------------
#Pushback(n) is passed the number of characters to push back. 
# For example, ii_pushback(5) pushes back the five most recently read characters. 
# If you try to push past the sMark, only the characters as far as the sMark are 
# pushed and 0 is returned (1 is returned on a successful push). If you push past the eMark, 
# the eMark is moved back to match the current character. Unlike ungetc(), you can 
# indeed push back characters after EOF has been reached.
#--------------------------------------------------
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
        
        n -= 1

    if (Input.Next < Input.eMark):
        Input.eMark =  Input.Next
        Input.Mline = Input.Lineno


    return( Input.Next > Input.sMark )    

#---------------------------------------------------
#                      Terminate Unterminate
# These routines are not-strictly speaking-necessary, because the lexeme 
# length is always available. It's occasionally useful to have a terminator on the string,
# however. Note that these functions should be used exclusively after the string has been
# terminated-the other input functions will not work properly in this case.

# This approach is better than putting the ii_unterm() code into ii_advance (),
# because the latter approach slows down all ii _advance() calls. On the other hand,
# you have to remember to call ii_unterm () before calling ii_advance(). For this
# reason, an ii_input () function has been provided to make sure that the
# lexeme is unterminated and then reterminated correctly. That is, ii_input () is a
# well-behaved input function meant to be used directly by the user.
#---------------------------------------------------
def ii_term():
    '''
    Saves the character pointed to by Next in a variable called Termchar, 
    and then overwrites the character with a' \0'.
    '''
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
    '''
    Reverse-input function. It backs up the input one notch and then overwrites 
    the character at that position with its argument. ii_unput() works correctly 
    on both terminated and unterminated buffers, unlike ii_pushback(), which 
    can't handle the terminator.
    '''
    if(Input.Termchar):
        ii_unterm()
        if( ii_pushback(1) ):
            Input.StartBuf[Input.Next] = c
            ii_term()
    else:
        if( ii_pushback(1)):
            Input.StartBuf[Input.Next] = c

#-------------------------------------
# 
#--------------------------------------
def ii_lookahead( n ):
    '''
    The ii_lookahead() function bears the same relation to ii_look() that 
    ii_input() bears to ii_advance(). That is, ii_lookahead(1) functions
    correctly for strings that have been terminated with ii_term() calls, ii_look() 
    does not. 
    '''
    return Input.Termchar if (n == 1 and Input.Termchar is not None) else ii_look(n)

def ii_flushbuf():
    '''
    ii_flushbuf() flushes a terminated buffer by unterminating 
    it before calling ii_flush().
    '''
    if (Input.Termchar is not None):    
        ii_unterm()
    return ii_flush(1)



#################################################
# Python3 program to rotate an array by  
# d elements  
# Function to left rotate arr[] of size n by d*/ 
    # Driver program to test above functions */ 
    # arr = array.array('B', [x for x in range(10)])
    # #arr = [1, 2, 3, 4, 5, 6, 7] 
    # leftRotate(arr, 2, 7) 
    # printArray(arr, 7) 
    
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
  

def skip_whitespace(c):
    ''' [ \t\n]* '''
    while c is not None and c.isspace():
        c = ii_advance()
        c = chr(c)

def integer(c):
    """Return a (multidigit) integer consumed from the input."""
    result = ''
    while c is not None and c.isdigit():
        result += c
        c = ii_advance()
    return int(result)

def printBuf():
    print(''.join([chr(c) for c in Input.StartBuf]))

if __name__ == '__main__':
    
    ii_io(open_funct, close_funct, read_funct)
    ii_newfile('./src/test_files/web.config') 
    #ii_newfile('./src/test_files/abcdefg.txt') 
    
    i = 1
    c = ii_advance()
    #print(f'c : {i} : {chr(c)}')
    # binary print(chr(c))
    print(c)
    
    while not NO_MORE_CHARS():
        i+=1
        c = ii_advance()
        if c != -1:
            pass
            #print(f'c : {i} - {chr(c)}')
            #print(chr(c))
        elif c == -1:
            print(f'i : {i}')
            ii_mark_prev()
            ii_mark_start()          
    printBuf()

    # while not NO_MORE_CHARS():

    #     # ignore whitespace
    #     if c in Input.whitespace:
    #         if c in Input.newline:
    #             Input.lineno += 1
    #             Input.linepos = 0
    #         c = chr(ii_advance())
    #         i += 1
    #         print(f'c : {i} - {c}')

    #     # comment
    #     elif c in Input.comment_marker:
    #         while c not in Input.newline:
    #             c = chr(ii_advance())
    #             i += 1
    #             print(f'c : {i} - {c}')


    #     # identifier token
    #     elif c in string.ascii_letters:
    #         match = char
    #         c = chr(ii_advance())
    #         i += 1
    #         print(f'c : {i} - {c}')

    #         while char in string.ascii_letters:
    #             match += char
    #             c = chr(ii_advance())
    #             i += 1
    #             print(f'c : {i} - {c}')