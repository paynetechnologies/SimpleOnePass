import sys
import string
from src.symbol_table import symbol_table
from src.constants import constants, entry
from src.error import error_message

class lexer():
    comment_marker = '#'
    eof_marker = '$'
    newline ='\n'
    whitespace = ' \t'
    operators = ['+', '-', '/', '*']

        # STRMAX = 999 # size of lexeme list
        # self.lexemes = ['' for i in range(symbol_table.STRMAX)]
        # self.last_char = -1 # last used position in lexemes


    def __init__(self):
        self.input_ptr = -1
        self.lexeme_buffer = [None] * constants.BUFFERSIZE
        #self.lexeme_buffer = ['' for i in range(constants.BUFFERSIZE)]
        self.lexeme_buffer_ptr = -1
        self.token_value = None    
        self.cursor = 1 # same as ptr
        self.tokens = [] 
        self.line_no = 0
        self.line_pos = 0

    def loadBuffer(self, input):
        self.inputBuffer = input
        self.lines = input.split(lexer.newline)

    def get_next_char(self):
        self.input_ptr += 1
        self.line_pos += 1

        if self.input_ptr >= len(self.inputBuffer):
            return lexer.eof_marker

        c = self.inputBuffer[self.input_ptr]
        return c

    def ungetchar(self):
        self.input_ptr -= 1

    def tokenizer(self):

        char = self.get_next_char()
        while (char != lexer.eof_marker):            

            # whitespace
            if (char in lexer.whitespace):
                constants.token_value = constants.WHITESPACE                
                while char in lexer.whitespace:
                    char = self.get_next_char()

            # newline
            elif (char in lexer.newline):
                constants.token_value = constants.NEWLINE
                while char in lexer.newline:
                    self.line_no += 1                    
                    self.line_pos = 0
                    char = self.get_next_char()

            # comment
            elif char in lexer.comment_marker:
                constants.token_value = constants.COMMENTS
                while char not in lexer.newline:
                    char = self.get_next_char()

            # number
            elif (char in string.digits):
                match = char
                constants.token_value = int(char) - 0
                char = self.get_next_char()
                
                while(char in string.digits):                    
                    match += char
                    constants.token_value = constants.token_value * 10 + int(char) - 0
                    char = self.get_next_char()
                self.ungetchar()                

                print(f'isdigit : {constants.token_value}')
                return constants.NUM

            # alpha and alphanumeric     
            elif (char.isalpha()):
                match = char
                char = self.get_next_char()
                while (char.isalnum()):
                    match += char
                    char = self.get_next_char()
                self.ungetchar()

                # lenValue = len(match)
                # if (self.last_char + lenValue > symbol_table.STRMAX ):
                #     error_message("lexeme list full")
                self.lexeme_buffer_ptr += 1
                if (self.lexeme_buffer_ptr >= constants.BUFFERSIZE):
                    error_message(constants.line_no,"compiler error :: Lexeme Buffer Overflow")                    

                self.lexeme_buffer[self.lexeme_buffer_ptr] = match

                # create string from slice of list
                # lexeme = ''.join(self.lexeme_buffer[:self.lexeme_buffer_ptr])

                lexeme = self.lexeme_buffer[self.lexeme_buffer_ptr]

                # Symbol Table Lookup and Insert
                symbol_table_index = None
                symbol_table_index = symbol_table.lookup(lexeme)

                if (symbol_table_index == None):
                    symbol_table_index = symbol_table.insert(lexeme, constants.ID)
                
                constants.token_value = symbol_table_index
                return constants.SYMBOL_TABLE[symbol_table_index].token
            
            # Operators
            elif ( char == "+"):
                constants.token_value = constants.PLUS
                return char 

            elif ( char == "-"):
                constants.token_value = constants.MINUS
                return char 

            elif ( char == "*"):
                constants.token_value = constants.MULTIPLY
                return char 

            elif ( char == "/"):
                constants.token_value = constants.DIVIDE
                return char

            # EOF
            elif (char == constants.EOF):
                constants.token_value = constants.EOF
                return constants.DONE

            # All others
            else:
                constants.token_value = constants.NONE
                return char
        
        return constants.EOF

if (__name__ == "__main__"):
    l = lexer()
    l.loadBuffer("   a")
    l.tokenizer()
