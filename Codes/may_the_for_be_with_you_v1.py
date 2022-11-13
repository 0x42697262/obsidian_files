"""
Notes:
        https://github.com/KrulYuno/obsidian_files/blob/master/Notes/020%20Studies/CMSC%20142%20Machine%20Problem%201.md
"""

import re

TOKEN_TYPE = {
        '{'     :  'OPEN_BRACE',
        '}'     :  'CLOSE_BRACE',
        '('     :  'OPEN_PAREN',
        ')'     :  'CLOSE_PAREN',
    #   KEYWORDS
        'if'    :  'KEYWORD',
        'else'  :  'KEYWORD',
        'for'   :  'KEYWORD',
    #   DATA TYPES
        'int'   :  'DATA_TYPE',
        'float' :  'DATA_TYPE',
        'char'  :  'DATA_TYPE',
        'void'  :  'DATA_TYPE',
        'bool'  :  'DATA_TYPE',
        'var'   :  'IDENTIFIER',
        ';'     :  'SEMICOLON',
        ','     :  'COMMA',
    #   something that costs T(n)
        '-='    :  'ASSIGN',
        '+='    :  'ASSIGN',
        '*='    :  'ASSIGN',
        '/='    :  'ASSIGN',
        '='     :  'ASSIGN',
        '>>'    :  'BITWISE',
        '<<'    :  'BITWISE',
    #   ARITHMETIC OPERATIONS
        '+'     :  'OPERATION',
        '-'     :  'OPERATION',
        '/'     :  'OPERATION',
        '*'     :  'OPERATION',
    #   CONDITIONAL OPERATIONS
        '<'     :  'OPERATION',
        '>'     :  'OPERATION',
        '<='    :  'OPERATION',
        '>='    :  'OPERATION',
        '=='    :  'OPERATION',
        '!='    :  'OPERATION',
    #   others
        'lit'   :  'LITERAL',
        }

identifier_chars = ['_']
for c in range(48, 58):
        identifier_chars.append(chr(c))
for c in range(65, 91):
        identifier_chars.append(chr(c))
for c in range(97, 123):
        identifier_chars.append(chr(c))

literal_chars = ['"', '\'']

def main():
    # Take inputs, assume inputs are correct
    # no sanitization
    lines = int(input())
    expression = str()
    for _ in range(lines):
        expression += input()



if __name__ == "__main__":
    main()
