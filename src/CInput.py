'''                                              LBufEnd       
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
   |<---- BUFSIZE=(3 x MAXLEX ) + (2 * MAXLOOK)------->|
'''
'''                                              
   Start_buf                       Next      DANGER    END
   |     pmark    smark        emark |         |LBufEnd |
   |     |        |            |     |         |    |   |
   v     v        v            v     v         v    v   v 
   +-------------------------------------------+---+---+
   |     |prev lex|current lex|                |YYY|XXX| Normally
   |-------------------------------------------|---|---|
   |                                                   |
   |<------------------- BUFSIZE --------------------->|
'''
'''                                              
   Start_buf                            DANGER        END
   |                           Next       |  LBufEnd   |
   v                            |         |     |      |
   pmark    smark       emark   |         |     v      v
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
import base64


class CInput:

    MAXLOOK = 16                               # max amount of lookahead
    MAXLEX  = 1024                             # max lexeme size
    BUFSIZE = (MAXLEX * 3) + (2 * MAXLOOK)     # Change the 3 only
    END = BUFSIZE                              # just past last char in buf

    # Input Buffer
    InputBuf = array.array('B', [126 for x in range(BUFSIZE)]) 
    
    MVInputBuf = memoryview(InputBuf)           # Memoryview of Input Buffer    

    LBufEnd = END  # logical buffer end...just past last char
    Next    = END   # Next input char
    sMark   = END   # start of current lexeme
    eMark   = END   # end of current lexeme
    pMark   = END   # start of previous lexeme
    pLineno = 0     # line # of previous lexeme
    pLength = 0     # length of previous lexeme

    STDIN = sys.stdin # default standard input

    inpFile     = STDIN  # input file handle
    Lineno      = 1     # current line number
    Linepos     = 0 
    Mline       = 1     # Line # when mark_end() is called
    Termchar    = 0     # holds the char that was overwritten by \0 when last char is null terminated

    been_called = True
    EOF         = True  # constant
    ''' 
    End of file has been read. It's possible for this to be true 
    and for characters to still be in the input buffer.
    '''
    EOF_Read    = False 
    fd = None                                           # file descriptor
    ii_io = {}                                          # pointers to Open, Read, Close functions


    def __init__(self, input_filename ):
        self.ii_ii(self.open_funct, self.close_funct, self.read_funct)
        self.ii_newfile(input_filename)         


    #---------------------------------------------------
    #                      I/O
    #---------------------------------------------------
    def open_funct(self, filename, mode, encoding=None):
        fd=open(filename, mode, encoding=encoding)
        return fd

    def close_funct(self):
        self.fd.close()

    def read_funct(self, fd, starting_at, need):

        begin_seek_pos = fd.tell()
        print(f'##### read_funct :: Seek at pos: {begin_seek_pos}')

        try:
            print(f'##### read_funct :: Read into MVInputBuf starting at pos: {starting_at}')
            fd.readinto(CInput.MVInputBuf[starting_at:])
        except EOFError:
            CInput.EOF_Read = True
            self.close_funct()
        except Exception as e :
            raise ValueError(f"READ Unexpected error : {e}", sys.exc_info()[0])
        
        got = min(fd.tell() - begin_seek_pos, need)
        print(f'##### read_funct :: {got} bytes' )

        print(f'##### read_funct :: Dumping MVInputBuf from {starting_at} to got {starting_at + got}' )
        print( ''.join( [chr(c) for c in CInput.MVInputBuf[starting_at:starting_at + got]] ) )

        return got

    def ii_ii(self, o, c, r):
        '''
        Used to change the low-level input functions that
        are used to open files and fill the buffer.
        '''
        CInput.ii_io["openp"] = o
        CInput.ii_io["closep"] = c
        CInput.ii_io["readp"] = r
        #print(CInput.ii_io)

    #---------------------------------------------------
    #                      Open Read File
    # The normal mechanism for opening a new input file. 
    # It is passed the file name and returns the file descriptor (not the
    # FILE pointer) for the opened file, or -1 if the file couldn't be opened. 
    # The previous input file is closed unless it was standard self. 
    # ii _new fi1e() does not actually read the first buffer; rather, it 
    # sets up the various pointers so that the buffer is loaded the first time a 
    # character is requested. This way, programs that never call ii_newfile() will
    # work successfully, getting input from standard self. The problem with this approach is
    # that you must read at least one character before you can look ahead in the input (otherwise
    # the buffer won't be initialized). If you need to look ahead before advancing, use:
    #     ii_advance(); Read first bufferfull of input 
    #     ii_pushback(l); but put back the first character 
    # The default input stream [used if ii newfile() is never called] is standard self.
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
    def ii_newfile(self, name=None):
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

        fd = self.STDIN if name is None else self.ii_io["openp"](name, 'rb')
        
        '''
        Note that the indirect open () call uses the 'rb' BINARY input mode. A CR-LF
        (carriage-return, linefeed) pair is not translated into a single '\n' when binary-mode
        input is active. This behavior is desirable in most LEX applications, which treat both CR
        and LF as white space. There's no point wasting time doing the translation. The lack of
        translation might cause problems if you're looking for an explicit '\n' in the input,
        though.
        '''
        if(fd != 0):   

            if self.inpFile != self.STDIN:
                self.ii_io["closep"](self.inpFile)

            self.inpFile = fd
            self.EOF_Read = False

            self.Next      = self.END
            self.sMark     = self.END
            self.eMark     = self.END
            self.LBufEnd    = self.END
            self.Lineno    = 1
            self.Mline     = 1
            self.fd = fd

        return fd

    def doStuff(self, chunk):
        lines = chunk.split(b'\n')
        for line in lines:
            print(line)


        #readfile_into_buffer("./test_files/web.config") #python self.py
        #readfile_into_buffer("./src/test_files/web.config") #DEBUG

    def readfile_into_buffer(self, filename):
        t1=0
        #t2=0

        self.ii_ii(self.open_funct, self.close_funct, self.read_funct)

        self.ii_io["openp"](filename, 'r')

        start = time.time()

        with open(filename, 'r') as f:
            for chunk in iter(lambda: f.read(self.BUFSIZE), b''):
                self.doStuff(chunk)
        end = time.time()

        t1 = end-start
        print(f't1 - {t1}')
        '''
        start = time.time()
        with open(filename, 'rb') as f:
            while True:
                chunk = f.read(self.BUFSIZE)
                if not chunk:
                    break
                doStuff(chunk)
        end = time.time()
        t2 = end - start
        '''
        
        #print(f't1 - {t1} : t2  {t2}')

    def chunk_file(self, fd, chunksize = BUFSIZE):
        return iter(lambda: fd.read(chunksize), b'')      


    #---------------------------------------------------
    #                      Access
    #---------------------------------------------------
    def ii_text(self):
        '''Pointer to current lexeme'''
        return self.sMark

    def ii_length(self):
        ''' lexeme length'''
        return self.eMark - self.sMark

    def ii_lineno(self):
        '''line number of last char in lexeme'''
        return self.Lineno

    def ii_ptext(self):
        '''Pointer to previous lexeme'''
        return self.pMark

    def ii_plength(self):
        '''previous lexeme length'''
        return self.pLength

    def ii_plineno(self):
        '''line number of last char in previsous lexeme'''
        return self.pLineno

    def ii_mark_start(self):
        '''
        Moves the sMark to the current input position (pointed to by Next). 
        It also makes sure that the end-of-lexeme marker (eMark) is not to 
        the left of the start marker.
        '''
        self.Mline = self.Lineno
        self.eMark = self.sMark = self.Next
        return self.sMark

    def ii_mark_end(self):
        '''
        Similar to ii_mark_start...
        It also saves the current line number in Mline, because the lexical analyzer 
        might sweep past a newline when it scans forward looking for a new lexeme. 
        The input line number must be restored to the condition it was in before the 
        extra newline was scanned when the analyzer returns to the previous end marker
        '''
        self.Mline = self.Lineno
        self.eMark = self.Next
        return self.eMark

    def ii_move_start(self):
        '''
        Move the start marker one space to the right. 
        It returns the new start marker on success, NULL if you tried to move past 
        the end marker (sMark is not modified in this last case). 
        '''
        if (self.sMark >= self.eMark):  
            return None  
        else: 
            self.sMark += 1
            return self.sMark

    def ii_to_mark(self):
        '''
        Restores the input pointer to the last end mark
        '''
        self.Lineno = self.Mline
        self.Next = self.eMark
        return self.Next

    def ii_mark_prev(self):
        '''
        Modifies the previous-lexeme marker to reference the same lexeme as the 
        current-lexeme marker. Typically, ii_mark_prev() is called by the lexical
        analyzer just before calling ii_mark_start() (that is, just before it begins 
        to search for the next lexeme ).
        Set the pMark. Note: a buffer flush won't go past pMark so
        once you save it, you must move it every time you move sMark.
        This is not done automatically, since you may want to 
        remember the token before last rather than the last one.
        If ii_mark_prev is never called, pMark is ignored, no worries;
        '''
        self.pMark = self.sMark
        self.pLineno = self.Lineno
        self.pLength = self.eMark - self.sMark
        return self.pMark
    
    def Need_Extra_newLine(self):     

        '''
        Push a newline on the empty buffer so LEX start-of-line
        will work on the first input line.
        Provided for those situations where you want an extra newline appended 
        to the beginning of a file. LEX needs this capability for processing the 
        start-of-line anchor-a mechanism for recognizing strings only if they appear 
        at the far left of a line. Such strings must be preceded by a newline, so an 
        extra newline has to be appended in front of the first line of the file; otherwise, 
        the anchored expression wouldn't be recognized on the first line.
        '''
        self.Next = self.sMark = self.eMark = self.END - 1
        
        # str
        # does this add to next or end of buffer
        # self.InputBuf[self.Next] = '\n'
        
        # byte array 
        # *Next = '\n'
        # self.membuf[self.Next] = '\n'
        CInput.MVInputBuf[self.Next] =  ord(b'\n')

        self.Lineno -= 1
        self.Mline -= 1
        self.been_called = True

    #---------------------------------------------------
    #             Buffer 
    #---------------------------------------------------

    # Flush buffer when Next passes this address
    def DANGER(self):
        return self.LBufEnd - self.MAXLOOK

    def NO_MORE_CHARS(self):
        if (self.EOF_Read and self.Next > self.LBufEnd):
            self.close_funct()
            return True
        return False
        
    #---------------------------------------------------
    #                      Advance & Flush
    #---------------------------------------------------
    def ii_advance(self, needFlush):
        '''
        ii_advance is the real input function. It returns the Next character
        from input and advances past it. The buffer is flushed if the current
        character is within MAXLOOK characters of the end of the buffer. 0 is
        returned at the end of file. -1 returned if the buffer can't be flushed
        because it's too full. In this case, you can call ii_flush(1) to do a
        buffer flush but you'll lose the curent lexeme as a result.
        '''
        if (not self.been_called):
            self.Need_Extra_newLine()

        if (self.NO_MORE_CHARS()):
            return 0

        if (not self.EOF_Read and (self.ii_flush(needFlush) < 0)):
            return -1

        if (CInput.MVInputBuf[self.Next] == ord('\n')): # if *Next = '\n' 
            self.Lineno += 1

        c = CInput.MVInputBuf[self.Next]

        self.Next +=1
        return (c)


    def ii_flush(self, force):
        '''
        Flush the input buffer. Do nothing if the current input characters isn't
        in the danger zone, otherwise move all unread characters to the left end
        of the buffer and fill the remainder of the buffer. Note that input()
        flushes the buffer willy-nilly if you read past the end of buffer.
        Similarly, input_line() flushes the buffer at the beginning of each line.
                                        
        Start_buf    pmark              DANGER              END
        |            |smark        emark  |Next      LBufEnd|
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
        left_edge = 0

        if (self.NO_MORE_CHARS()):
            return 0

        if (self.EOF_Read):    # nothing more to read
            return 1

        if (self.Next >= self.DANGER() or force):        
            left_edge = min(self.sMark, self.pMark) if self.pMark > 0 else self.sMark
            
            shift_amt = left_edge - 0

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

            if (shift_amt < self.MAXLEX): # if not enough room 
                if (not force):
                    return -1

                left_edge = self.ii_mark_start() # reset start to current character
                self.ii_mark_prev()
                shift_amt = left_edge - 1 # if using pointers: shift_amt = left_edge - self.InputBuf

            # How many characters have to be copied (copy_ amt) 
            # and the distance that they have to be moved (shift_amt).
            copy_amt = self.LBufEnd - left_edge

            if copy_amt > 0:
                arr = array.array('B', CInput.MVInputBuf)
                arr = self.left_rotation(arr,left_edge)
                CInput.MVInputBuf = memoryview(arr)

            if (not self.ii_fillBuf(copy_amt)): 
                print(f"????? INTERNAL ERROR, ii_flush: Buffer full, can't read \n")
            
            if (self.pMark > 0):
                self.pMark -= shift_amt

            self.sMark -= shift_amt
            self.eMark -= shift_amt
            self.Next -= shift_amt

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
    def ii_fillBuf(self, starting_at):
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
        need = 0                # number of bytes needed from input
        got = 0                 # number of bytes actually read

        need = int((( self.END  - starting_at) / self.MAXLEX) * self.MAXLEX)

        if (need < 0):
            print(f'INTERNAL ERROR ii_filBuf() : Bad rea-request starting addr. \n')
            return -1

        if (need == 0):
            return 0

        # do the read
        got = self.ii_io["readp"](self.inpFile, starting_at, need)

        if (got == None):
            print(f"Can't read input file. \n")
            return -1

        self.LBufEnd = starting_at + got

        if (got < need):
            self.EOF_Read = True

        return got


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
    def ii_look(self, n):
        '''
        Return the nth character of lookahead, EOF if you try to look past
        end of file, or 0 if you try to look past either end of the buffer.
        '''
        p = None
        p = self.Next + (n - 1)

        if (self.EOF_Read and p >= self.LBufEnd):
            return self.EOF

        return 0 if (p < 0 or p >= self.LBufEnd) else CInput.MVInputBuf[p]


    #------------------------------------------------
    # Pushback(n) is passed the number of characters to push back. 
    # For example, ii_pushback(5) pushes back the five most recently read characters. 
    # If you try to push past the sMark, only the characters as far as the sMark are 
    # pushed and 0 is returned (1 is returned on a successful push). If you push past the eMark, 
    # the eMark is moved back to match the current character. Unlike ungetc(), you can 
    # indeed push back characters after EOF has been reached.
    #--------------------------------------------------
    def ii_pushback(self, n):
        '''
        Push n characters back into the self. You can't push past the current
        sMark. You can, however, push back characters after end of file has
        been encountered.
        '''
        n -= 1
        while ( n >= 0 and self.Next > self.sMark):
            
            if( CInput.MVInputBuf[self.Next] == '\n' or self.Next == 0):
                self.Lineno -= 1
            
            n -= 1

        if (self.Next < self.eMark):
            self.eMark =  self.Next
            self.Mline = self.Lineno
            
        return( self.Next > self.sMark )    

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
    def ii_term(self):
        '''
        Saves the character pointed to by Next in a variable called Termchar, 
        and then overwrites the character with a' \0'.
        '''
        self.Termchar = CInput.MVInputBuf[self.Next]
        CInput.MVInputBuf[self.Next] = b'\0'

    def ii_unterm(self):
        if( self.Termchar):
            CInput.MVInputBuf[self.Next] = self.Termchar
            self.Termchar = 0

    def ii_input(self):
        rval = None
        
        if(self.Termchar):
            self.ii_unterm()
            rval = self.ii_advance(0)
            self.ii_mark_end()
            self.ii_term()
        else:
            rval = self.ii_advance(0)
            self.ii_mark_end ()
        return rval

    def ii_unput(self,c):
        '''
        Reverse-input function. It backs up the input one notch and then overwrites 
        the character at that position with its argument. ii_unput() works correctly 
        on both terminated and unterminated buffers, unlike ii_pushback(), which 
        can't handle the terminator.
        '''
        if(self.Termchar):
            self.ii_unterm()
            if( self.ii_pushback(1) ):
                CInput.MVInputBuf[self.Next] = bytes(c)
                self.ii_term()
        else:
            if( self.ii_pushback(1)):
                CInput.MVInputBuf[self.Next] = bytes(c)

    def ii_lookahead(self, n ):
        '''
        The ii_lookahead() function bears the same relation to ii_look() that 
        ii_input() bears to ii_advance(). That is, ii_lookahead(1) functions
        correctly for strings that have been terminated with ii_term() calls, ii_look() 
        does not. 
        '''
        return self.Termchar if (n == 1 and self.Termchar is not None) else self.ii_look(n)

    def ii_flushbuf(self):
        '''
        ii_flushbuf() flushes a terminated buffer by unterminating 
        it before calling ii_flush().
        '''
        if (self.Termchar is not None):    
            self.ii_unterm()
        return self.ii_flush(1)

    #---------------------------------------------------
    #                      Copy Shift
    #---------------------------------------------------
    def left_rotation(self, a, k):
        # if the size of k > len(a), rotate only necessary with
        # module of the division
        rotations = k % len(a)
        return a[rotations:] + a[:rotations]

    def leftRotate(self,arr, d, n): 
        self.printArrays(arr, n)
        for _ in range(d): 
            self.leftRotatebyOne(arr, n) 
    
    # Function to left Rotate arr[] of size n by 1*/  
    def leftRotatebyOne(self,arr, n): 
        temp = chr(126)
        for i in range(n-1): 
            arr[i] = arr[i + 1] 
        arr[n-1] = temp 
            
    #-------------------------------------
    #              PRINT
    #--------------------------------------
    #             
    # utility function to print an array */ 
    def printArrays(self, arr, size): 
        for i in range(size):
            print ("% d"% arr[i], end =" ") 
            #print ("% s"% arr[i], end =" ")     

    # utility function to print an array */ 
    def printArray2(self, arr, size): 
        for i in range(size): 
            print ("% s"% chr(arr[i]), end ="") 
        print('##### END OF ARRAY')

    def printBuf(self):
        print(''.join([chr(c) for c in CInput.MVInputBuf]))
