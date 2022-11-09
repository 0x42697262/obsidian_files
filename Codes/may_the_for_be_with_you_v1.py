"""
Reference:
    https://github.com/huzaifamaw/Lexical_Analyzer-Parser_Implemented-in-Python/blob/master/main.py
"""

import re

TOKEN_DEFINITION = {
        '='  : 'ASSIGN',
        '<'  : 'LESS_THAN',
        '>'  : 'GREATER_THAN',
        '++' : 'SELF_PLUS',
        '--' : 'SELF_MINUS',
        '+'  : 'PLUS_OPERATOR',
        '-'  : 'MINUS_OPERATOR',
        '*'  : 'MULTIPLY_OPERATOR',
        '/'  : 'DIVIDE_OPERATOR',
        '<=' : 'LESS_THAN_EQUAL',
        '>=' : 'GREATER_THAN_EQUAL',
        '+=' : 'PLUS_EQUAL',
        '-=' : 'MINUS_EQUAL',
        '*=' : 'MULTIPLY_EQUAL',
        '/=' : 'DIVIDE_EQUAL',
        '('  : 'OPEN_PARENTHESIS',
        ')'  : 'CLOSE_PARENTHESIS',
        '['  : 'OPEN_BRACKET',
        ']'  : 'CLOSE_BRACKET',
        '{'  : 'OPEN_BRACE',
        '}'  : 'CLOSE_BRACE',
        ','  : 'COMMA',
        '"'  : 'DOUBLE_QUOTE',
        '\'' : 'SINGLE_QUOTE',
        ';'  : 'SEMICOLON',
        '&&' : 'AND',
        '||' : 'OR',
        '<<' : 'LEFT_BITWISE',
        '>>' : 'RIGHT_BITWISE',
        '==' : 'IF_EQUAL',
        }

TOKEN_KEYWORD = {
        'strict'     :  ["if", "else", "while", "for", "cout", "cin", "return"],
        'brackets'   :  ['(', ')', '{', '}', '[', ']'],
        'data_types' :  ["int", "float", "char", "string", "bool", "void"],
        'arithmetic' :  ['+', '-', '/', '*'],
        'logical'    :  ['||', '&&'],
        } 

class Lexer:
    def __init__(self) -> None:
        pass


class Parser:
    def __init__(self, expression: str) -> None:
        self.expression = expression
        print(self.expression)

    def tokenize(self) -> None:
        lex = Lexer()
        


def main():
    # Take inputs, assume inputs are correct
    # no sanitization
    lines = int(input())
    expression = str()
    for _ in range(lines):
        expression += input()

    p = Parser(expression)
    p.tokenize()


if __name__ == "__main__":
    main()
