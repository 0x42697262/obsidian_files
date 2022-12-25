"""
Notes:
        https://github.com/KrulYuno/obsidian_files/blob/master/Notes/020%20Studies/CMSC%20142%20Machine%20Problem%201.md
References:
        https://github.com/Esamanoaz/plox
"""

from enum import Enum, auto



##
#
#   TOKENS
#
##

class TokenType(Enum):
    # single character tokens 
    OPEN_PAREN          = auto() # (
    CLOSE_PAREN         = auto() # }
    OPEN_BRACE          = auto() # {
    CLOSE_BRACE         = auto() # }
    OPEN_BRACKET        = auto() # [
    CLOSE_BRACKET       = auto() # ]
    COMMA               = auto() # ,
    DOT                 = auto() # .
    COLON               = auto() # :
    SEMICOLON           = auto() # ;
    BACKWARD_SLASH      = auto() # \

    # one or two character tokens
    LOGICAL_AND         = auto() # &&
    LOGICAL_OR          = auto() # ||
    BANG                = auto() # !
    BANG_EQUAL          = auto() # !=
    EQUAL               = auto() # =
    EQUAL_EQUAL         = auto() # ==
    GREATER             = auto() # >
    GREATER_GREATER     = auto() # >>
    GREATER_EQUAL       = auto() # >=
    LESSER              = auto() # <
    LESSER_LESSER       = auto() # <<
    LESSER_EQUAL        = auto() # <=
    PLUS                = auto() # +
    PLUS_PLUS           = auto() # ++
    PLUS_EQUAL          = auto() # +=
    MINUS               = auto() # -
    MINUS_MINUS         = auto() # --
    MINUS_EQUAL         = auto() # -=
    STAR                = auto() # *
    STAR_STAR           = auto() # **
    STAR_EQUAL          = auto() # *=
    SLASH               = auto() # /
    SLASH_SLASH         = auto() # //
    SLASH_EQUAL         = auto() # /= 

    # literals
    IDENTIFIER          = auto()
    STRING              = auto()
    NUMBER              = auto()

    # keywords
    TRUE                = auto() # true
    FALSE               = auto() # false 
    IF                  = auto() # if
    ELSE                = auto() # else
    FOR                 = auto() # for
    CIN                 = auto() # cin 
    COUT                = auto() # cout 
    RETURN              = auto() # return
    WHILE               = auto() # while
    INT                 = auto() # int
    CHAR                = auto() # char
    FLOAT               = auto() # float
    VOID                = auto() # void
    BOOL                = auto() # bool

    # EOF
    EOF                 = auto()


class Token:
    def __init__(self, _type, lexeme, literal, line) -> None:
       self.type        = _type
       self.lexeme      = lexeme
       self.literal     = literal
       self.line        = line

    def __str__(self):
        return f"Token<{self.type} : {self.lexeme}, {self.literal}> ({self.line})"


##
#
#  LEXICAL ANALYZER 
#
##

class Scanner:
    def __init__(self, source: list) -> None:
        self.source             = source
        self.tokens             = list()

        self.start_char         = 0
        self.current_char       = 0
        self.line               = 1
        self.index              = 0

        self.alpha              = ['_']                                             # [a-zA-Z_]
        self.digits             = [chr(c) for c in range(48, 58)]                   # [0-9]
        
        for _ in [chr(c) for c in range(97, 123)]:
                self.alpha.append(_)
        for _ in [chr(c) for c in range(65, 91)]:
                self.alpha.append(_)

        self.token_strings  = {
                '('      :      lambda c: TokenType.OPEN_PAREN,        
                ')'      :      lambda c: TokenType.CLOSE_PAREN,        
                '['      :      lambda c: TokenType.OPEN_BRACKET,        
                ']'      :      lambda c: TokenType.CLOSE_BRACKET,        
                '{'      :      lambda c: TokenType.OPEN_BRACE,        
                '}'      :      lambda c: TokenType.CLOSE_BRACE,        
                ','      :      lambda c: TokenType.COMMA,        
                '.'      :      lambda c: TokenType.DOT,        
                ':'      :      lambda c: TokenType.COLON,        
                ';'      :      lambda c: TokenType.SEMICOLON,        
                '\\'     :      lambda c: TokenType.BACKWARD_SLASH,        


        }

        self.keywords       = {
            'true'      :       TokenType.TRUE,
            'false'     :       TokenType.FALSE,
            'if'        :       TokenType.IF,
            'else'      :       TokenType.ELSE,
            'for'       :       TokenType.FOR,
            'cin'       :       TokenType.CIN,
            'cout'      :       TokenType.COUT,
            'return'    :       TokenType.RETURN,
            'while'     :       TokenType.WHILE,
            'int'       :       TokenType.INT,
            'char'      :       TokenType.CHAR,
            'float'     :       TokenType.FLOAT,
            'bool'      :       TokenType.BOOL,
            'void'      :       TokenType.VOID,
        }


    def _peek(self):
        if self.is_eof():
            return "\0"
        return self.source[self.index][self.current_char]

    def _peek_next(self):
        if self.current_char + 1 >= len(self.source[self.index]):
            return "\0"
        return self.source[self.index][self.current_char + 1]

    def is_digit(self, c):
        return c in self.digits

    def is_alpha(self, c):
        return c in self.alpha

    def is_alphanum(self, c):
        return self.is_alpha(c) or self.is_digit(c)
    
    def is_eof(self):
        return self.current_char >= len(self.source[self.index])

    
    def _advance(self):
        self.current_char += 1

        return self.source[self.index][self.current_char - 1]

    def _add_token(self, token_type, literal = None):
        text = self.source[self.index][self.start_char : self.current_char]
        self.tokens.append(Token(token_type, text, literal, self.line))

    def _advance_line(self):
        self.line   += 1
        self.index  += 1


    def _match(self, expected) -> bool:
        if self.is_eof():
            return False
        elif self.source[self.index][self.current_char] != expected:
            return False
        else:
            self.current_char += 1
            return True


    def scan_token(self):
        while not self.is_eof():
            self.start_char = self.current_char
            print("CHAR:",self.start_char,self.source[self.index][self.start_char])
            self._scan_token()


        self.tokens.append(Token(TokenType.EOF, '', None, self.line))
        return self.tokens

    def _scan_token(self):
        c = self._advance()
        if c in self.token_strings:
            c = self.token_strings[c](c)
            if c is not None:
                self._add_token(c)
        elif self.is_digit(c):
            self._number_logic()
        elif self.is_alpha(c):
            self._identifier_logic()
        else:
            # self.interpreter.error(line=self.line, message="Unexpected character.")
            print(f"Unexpected character on line {self.line}")


    def _number_logic(self):
        while self.is_digit(self._peek()):
            self._advance()

        if self._peek() == '.' and self.is_digit(self._peek_next()):
            self._advance()
            
            while self.is_digit(self._peek()):
                self._advance()

        self._add_token(TokenType.NUMBER, float(self.source[self.index][self.start_char : self.current_char]))


    def _identifier_logic(self):
        while self.is_alphanum(self._peek()):
            self._advance()

        text        = self.source[self.index][self.start_char : self.current_char]
        token_type  = self.keywords.get(text)
        
        if token_type is None:
            token_type = TokenType.IDENTIFIER

        self._add_token(token_type)

    
    def _string_logic(self):
        starting_line = self.line
        while self._peek() != '\'' and not self.is_eof():
            self._advance()
        
        if self.is_eof():
            print(f"Expected ' at end of string on line {starting_line}")
            return None

        self._advance()

        self._add_token(TokenType.STRING, self.source[self.index][self.start_char+1 : self.current_char-1])


    
          

def main():
    # Take inputs, assume inputs are correct
    # no sanitization
    lines = int(input())
    source_code = list()
    for _ in range(lines):
        source_code.append(input())

    print(source_code)

    test = Scanner(source_code)
    t = list(test.scan_token())


    print("----")
    for _ in t:
        print(_.lexeme)


if __name__ == "__main__":
    main()
