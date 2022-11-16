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
    def __init__(self, source: str) -> None:
        self.source     = source
        self.tokens     = list()

        self.start      = 0
        self.current    = 0
        self.line       = 1

        self.alpha      = ['_']                                             # [a-zA-Z_]
        self.digits     = [chr(c) for c in range(48, 58)]                   # [0-9]
        
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
        return self.source[self.current]

    def _peek_next(self):
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def is_digit(self, c):
        return c in self.digits

    def is_alpha(self, c):
        return c in self.alpha

    def is_alphanum(self, c):
        return self.is_alpha(c) or self.is_digit(c)
    
    def is_eof(self):
        return self.current >= len(self.source)

          

def main():
    # Take inputs, assume inputs are correct
    # no sanitization
    lines = int(input())
    source_code = list()
    for _ in range(lines):
        source_code.append(input())

if __name__ == "__main__":
    main()
