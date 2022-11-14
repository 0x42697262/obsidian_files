"""
Notes:
        https://github.com/KrulYuno/obsidian_files/blob/master/Notes/020%20Studies/CMSC%20142%20Machine%20Problem%201.md
"""

import re

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
          

def main():
    # Take inputs, assume inputs are correct
    # no sanitization
    lines = int(input())
    source_code = list()
    for _ in range(lines):
        source_code.append(input())

if __name__ == "__main__":
    main()
