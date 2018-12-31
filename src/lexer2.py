import string


class Token(object):
    eof = 'EOF'
    ident = 'IDENT'
    number = 'NUMBER'
    operator = 'OP'
    punctuator = 'PUNC'
    keyword = 'KEYWORD'
    block_start = 'START'
    block_end = 'END'

    keywords = ['if', 'else', 'while', 'output']    

    def __init__(self, type, value, line, line_no, line_pos):
        self.type = type
        self.value = value
        self.line = line
        self.line_pos = line_pos - len(value)
        self.line_no = line_no

    def __str__(self):
        return '{0}:{1}'.format(self.line_no + 1, self.line_pos).ljust(10) + self.type.ljust(15) + self.value


class Lexer(object):

    eof_marker = '$'
    whitespace = ' \t\n'
    newline = '\n'
    comment_marker = '#'

    def __init__(self, code):
        super(Lexer, self).__init__()

        self.code = code
        self.cursor = 0
        self.tokens = []

        self.lines = code.split(Lexer.newline)
        self.line_no = 0
        self.line_pos = 0

    def get_next_char(self):
        self.cursor += 1
        self.line_pos += 1
        if self.cursor > len(self.code):
            return Lexer.eof_marker

        return self.code[self.cursor - 1]

    def tokenise(self):
        char = self.get_next_char()
        while char != Lexer.eof_marker:

            # ignore whitespace
            if char in Lexer.whitespace:
                if char in Lexer.newline:
                    self.line_no += 1
                    self.line_pos = 0
                char = self.get_next_char()

            # comment
            elif char in Lexer.comment_marker:
                while char not in Lexer.newline:
                    char = self.get_next_char()

            # identifier token
            elif char in string.ascii_letters:
                match = char
                char = self.get_next_char()
                while char in string.ascii_letters:
                    match += char
                    char = self.get_next_char()
                token = Token(Token.ident, match, self.lines[self.line_no], self.line_no, self.line_pos)
                
                if match in Token.keywords:
                    token.type = Token.keyword

                self.tokens.append(token)

            # number token
            elif char in string.digits:
                match = char
                char = self.get_next_char()
                #token.type = Token.number
                while char in string.digits:
                    match += char
                    char = self.get_next_char()

                token = Token(Token.number, match, self.lines[self.line_no], self.line_no, self.line_pos)
                self.tokens.append(token)

            # operators
            elif char in '+-*/=<>!':
                token = Token(Token.operator, char, self.lines[self.line_no], self.line_no, self.line_pos)
                self.tokens.append(token)
                char = self.get_next_char()

            # punctuators
            elif char in ':[](),;#':
                token = Token(Token.punctuator, char, self.lines[self.line_no], self.line_no, self.line_pos)
                self.tokens.append(token)
                char = self.get_next_char()                

            # start block
            elif char == '{':
                token = Token(Token.block_start, char, self.lines[self.line_no], self.line_no, self.line_pos)
                self.tokens.append(token)
                char = self.get_next_char()

            # end block
            elif char == '}':
                token = Token(Token.block_end, char, self.lines[self.line_no], self.line_no, self.line_pos)
                self.tokens.append(token)
                char = self.get_next_char()

            else:
                raise ValueError('Unexpected character found: {0}:{1} -> {2}\n{3}'.format(self.line_no + 1, self.line_pos + 1, char, self.lines[self.line_no]))


        # end of file token
        token = Token(Token.eof, char, None, self.line_no, self.line_pos)
        self.tokens.append(token)

        return self.tokens


if __name__ == '__main__':
    lexer = Lexer('Abc + Bcd = Cde')
    token = lexer.tokenise()        

    # on EOF, print the tokens    
    for token in lexer.tokens:
        print(token)