"""
Notes:
        https://github.com/KrulYuno/obsidian_files/blob/master/Notes/020%20Studies/CMSC%20142%20Machine%20Problem%201.md
References:
        https://github.com/Esamanoaz/plox
"""

import re
from enum import Enum, auto

identifier_chars = ['_']
lower_letters = [chr(c) for c in range(97, 123)]
upper_letters = [chr(c) for c in range(65, 91)]
digits = [chr(c) for c in range(48, 58)]

for _ in digits:
        identifier_chars.append(_)
for _ in lower_letters:
        identifier_chars.append(_)
for _ in upper_letters:
        identifier_chars.append(_)

literal_chars = ['"', '\'']

class TokenType(Enum):
    # single character tokens 
    OPEN_PAREN          = auto() # {
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





def Token_Type(token: str) -> str:
    match token:
        case '(':
            return "OPEN_PAREN"
        case ')':
            return "CLOSE_PAREN"
        case '{':
            return "OPEN_BRACE"
        case '}':
            return "CLOSE_BRACE"
        case '[':
            return "OPEN_BRACKET"
        case ']':
            return "CLOSE_BRACKET"
        case ';':
            return "SEMICOLON"
        case ':':
            return "COLON"
        case ',':
            return "COMMA"
        case '.':
            return "DOT"
        case '+':
            return "PLUS"
        case '-':
            return "MINUS"
        case '*':
            return "STAR"
        case '/':
            return "FORWARD_SLASH"
        case '\\':
            return "BACKWARD_SLASH"
        case _:
            return "ILLEGAL"


class Scanner:
    def __init__(self, source: str) -> None:
        self.source = source
        self.tokens = list()

        self.start = 0
        self.current = 0
        self.line = 1
    
    def is_eof(self):
        return self.current >= len(self.source)

    def next(self):

          

def main():
    # Take inputs, assume inputs are correct
    # no sanitization
    lines = int(input())
    source_code = list()
    for _ in range(lines):
        source_code.append(input())

if __name__ == "__main__":
    main()
