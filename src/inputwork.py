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

class Input:

    MAXLOOK = 16        # max amount of lookahead
    MAXLEX = 1024       # max lexeme size
    BUFSIZE = (MAXLEX * 3) + (2 * MAXLOOK)      # Change the 3 only

    startBuf = [None for x in range(BUFSIZE)]   # input buffer
    startBufA = array.array('c',[None for x in range(BUFSIZE)])

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

    def ii_newfile(name):

        fd=''

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



if __name__ == '__main__':
    Input.ii_newfile("./src/tests/tokenize-example-2.py")
