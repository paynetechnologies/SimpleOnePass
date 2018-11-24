import sys
import string
from src.symbol_table import SymbolTable, Entry
from src.error import lex_error_message
from src.token import Token


class lexer():
    
    BUFFERSIZE   = 128
    comment_marker = '#'
    eof_marker = '$'
    newline ='\n'
    whitespace = ' \t\n'
    operators = ['+', '-', '/', '*', 'MOD', 'DIV']


    # STRMAX = 999 # size of lexeme list
    # self.lexemes = ['' for i in range(SymbolTable.STRMAX)]
    # self.last_char = -1 # last used position in lexemes

    def __init__(self):
        
        self.input_ptr = -1
        self.line_no = 0
        self.line_pos = 0

        self.lexeme_buffer = [None] * lexer.BUFFERSIZE
        self.lexeme_buffer_ptr = -1

        self.token_value = None    
        self.tokens = [] 


    def loadBuffer(self, input):
        self.inputBuffer = input
        self.lines = input.split(lexer.newline)


    def get_next_char(self):
        self.input_ptr += 1
        self.line_pos += 1

        if self.input_ptr >= len(self.inputBuffer):
            return lexer.eof_marker

        return self.inputBuffer[self.input_ptr]


    def ungetchar(self):
        self.input_ptr -= 1


    def tokenizer(self):

        char = self.get_next_char()

        while (char != lexer.eof_marker):            

            # whitespace
            if (char in lexer.whitespace):
                while char in lexer.whitespace:
                    char = self.get_next_char()

            # newline
            elif (char in lexer.newline):
                while char in lexer.newline:
                    self.line_no += 1                    
                    self.line_pos = 0
                    char = self.get_next_char()

            # comment
            elif char in lexer.comment_marker:
                while char not in lexer.newline:
                    char = self.get_next_char()

            # number
            elif (char in string.digits):
                match = char
                Token.token_value = int(char) - 0
                char = self.get_next_char()
                
                while(char in string.digits):                    
                    match += char
                    Token.token_value = Token.token_value * 10 + int(char) - 0
                    char = self.get_next_char()
                self.ungetchar()                

                token = Token(Token.NUM, char, self.lines[self.line_no], self.line_no, self.line_pos)
                self.tokens.append(token)                   
                return Token.NUM

            # alpha and alphanumeric     
            elif (char.isalpha()):
                lexeme = char
                char = self.get_next_char()
                
                while (char.isalnum()):
                    lexeme += char
                    char = self.get_next_char()
                self.ungetchar()

                self.lexeme_buffer_ptr += 1

                if (self.lexeme_buffer_ptr >= lexer.BUFFERSIZE):
                    lex_error_message(self.line_no,"compiler error :: Lexeme Buffer Overflow")                    

                self.lexeme_buffer[self.lexeme_buffer_ptr] = lexeme

                # create string from slice of list
                # lexeme = ''.join(self.lexeme_buffer[:self.lexeme_buffer_ptr])

                #lexeme = self.lexeme_buffer[self.lexeme_buffer_ptr]

                Token.type = Token.IDENT
                if lexeme in Token.keywords:
                    Token.type = Token.KEYWORD

                token = Token(Token.type, lexeme, self.lines[self.line_no], self.line_no, self.line_pos)
                self.tokens.append(token)

                # Symbol Table Lookup and Insert
                symtbl_index = None
                symtbl_index = SymbolTable.lookup(lexeme)

                if (symtbl_index == None):
                    symtbl_index = SymbolTable.add(Token.ID, lexeme)

                Token.token_value = symtbl_index #token value is the index into the symbol table via emitter
                return SymbolTable.symbol_table[symtbl_index].token

            
            # Operators
            elif ( char == "+"):
                Token.token_value = Token.PLUS
                token = Token(Token.PLUS, char, self.lines[self.line_no], self.line_no, self.line_pos)
                self.tokens.append(token)                   
                return char 

            elif ( char == "-"):
                Token.token_value = Token.MINUS
                token = Token(Token.MINUS, char, self.lines[self.line_no], self.line_no, self.line_pos)
                self.tokens.append(token)                   
                return char 

            elif ( char == "*"):
                Token.token_value = Token.MULTIPLY
                token = Token(Token.MULTIPLY, char, self.lines[self.line_no], self.line_no, self.line_pos)
                self.tokens.append(token)                
                return char 

            elif ( char == "/"):
                Token.token_value = Token.DIVIDE
                token = Token(Token.DIVIDE, char, self.lines[self.line_no], self.line_no, self.line_pos)
                self.tokens.append(token)                
                return char

            # EOF
            elif (char == Token.EOF):
                Token.token_value = Token.EOF
                token = Token(Token.EOF, char, self.lines[self.line_no], self.line_no, self.line_pos)
                self.tokens.append(token)                
                return Token.DONE

            # All others
            else:
                Token.token_value = Token.NONE
                token = Token(Token.NONE, char, self.lines[self.line_no], self.line_no, self.line_pos)
                self.tokens.append(token)                
                return char

        token = Token(Token.EOF, char, self.lines[self.line_no], self.line_no, self.line_pos)
        self.tokens.append(token)                
        return Token.EOF

if (__name__ == "__main__"):
    l = lexer()
    l.loadBuffer("   a")
    l.tokenizer()
