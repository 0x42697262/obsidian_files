"""
Reference:
    https://github.com/huzaifamaw/Lexical_Analyzer-Parser_Implemented-in-Python/blob/master/main.py
"""

import re

# KEYWORDS = ['for', 'while', 'if', 'else', 'return', 
#             'cin', 'cout', 'int', 'float', 'char', 
#             'void', 'bool'
#             ]
#
TOKEN_TYPE = {
        '{'     :  'OPEN_BRACE',
        '}'     :  'CLOSE_BRACE',
        '('     :  'OPEN_PAREN',
        ')'     :  'CLOSE_PAREN',
        'if'    :  'KEYWORD',
        'else'  :  'KEYWORD',
        }

counts = ['+', '-', '*', '/', '%', '++', '--', '==', '!=',
          '>', '<', '>=','<=', '&&', '||', '//', '**',
          '>>', '<<', '+=', '-=', '*=', '/=',] 

class Lexer:
    def __init__(self, expr: str) -> None:
        self.expr = expr
        self.tokens = list()

        self.cursor = -1

    def next(self):
        self.cursor += 1
        while self.expr[self.cursor] == ' ':
            self.cursor += 1

    def peek(self):
        if self.cursor + 1 < len(self.expr):
            return self.expr[self.cursor + 1]

    def insert_token(self, token):
        print(f"Token: {token}")
        self.tokens.insert(len(self.tokens), token)

    def statement(self):
        self.compound_stmt()
        self.conditional_statement()

    def compound_stmt(self):
        if self.peek() == '{':
            self.next()
            self.insert_token(TOKEN_TYPE[self.expr[self.cursor]])
            self.statement()
            if self.peek() == '}':
                self.next()
                self.insert_token(TOKEN_TYPE[self.expr[self.cursor]])

    def conditional_statement(self):
        if self.peek() == 'i':
            self.next()
            if self.peek() == 'f':
                self.next()
                self.insert_token(TOKEN_TYPE['if'])
                if self.peek() == '(':
                    self.next()
                    self.insert_token(TOKEN_TYPE[self.expr[self.cursor]])
                    self.expression()
                    if self.peek() == ')':
                        self.next()
                        self.insert_token(TOKEN_TYPE[')'])
                        self.statement()

    def expression(self):
        pass


class Counter:
    def __init__(self, expr) -> None:
        self.t_n = 0
        self.input_expr = expr.split(';')

        for statement in self.input_expr:
            self.t_n += statement.count('=') + \
                    statement.count('+') + \
                    statement.count('-') + \
                    statement.count('*') + \
                    statement.count('/') + \
                    statement.count('%') + \
                    statement.count('++') + \
                    statement.count('--') + \
                    statement.count('==') + \
                    statement.count('!=') + \
                    statement.count('>') + \
                    statement.count('<') + \
                    statement.count('>=') + \
                    statement.count('<=') + \
                    statement.count('&&') + \
                    statement.count('||') + \
                    statement.count('//') + \
                    statement.count('**') + \
                    statement.count('>>') + \
                    statement.count('<<') + \
                    statement.count('+=') + \
                    statement.count('-=') + \
                    statement.count('*=') + \
                    statement.count('/=')

    def get_n(self) -> int:
        return self.t_n




def main():
    # Take inputs, assume inputs are correct
    # no sanitization
    lines = int(input())
    expression = str()
    for _ in range(lines):
        expression += input()

    c = Counter(expression)
    print(    c.get_n())
    l = Lexer(expression)
    l.statement()
    print(l.tokens)

if __name__ == "__main__":
    main()
