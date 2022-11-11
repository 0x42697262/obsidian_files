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

    def next(self, i=1):
        self.cursor += i
        self.skip_ws()

    def skip_ws(self):
        while self.peek() == ' ':
            self.cursor += 1

    def peek(self, i=1):
        if self.cursor + 1 < len(self.expr):
            return self.expr[self.cursor + i]


    def insert_token(self, token):
        print(f"Token: {token}")
        self.tokens.insert(len(self.tokens), token)

    def statement(self):
        self.skip_ws()
        self.compound_stmt()
        self.conditional_statement()
        self.for_loop()
        self.return_statement()
        self.var_definition()
        self.expression_statement()
        self.no_op()

    def compound_stmt(self):
        if self.peek() == '{':
            self.next()
            self.statement()

            if self.peek() == '}':
                self.next()
       
    def conditional_statement(self):
        if self.peek() == 'i' and self.peek(2) == 'f':
            self.next(2)
            if self.peek() == '(':
                self.next()
                self.expression()

                if self.peek() == ')':
                    self.next()
                    self.statement()
    
    def for_loop(self):
        if self.peek() == 'f' \
            and self.peek(2) == 'o' \
            and self.peek(3) == 'r':
                self.next(3)

                if self.peek() == '(':
                    self.next()
                    self.expression()

                    if self.peek() == ')':
                        self.next()
                        self.statement()

    def return_statement(self):
        pass

    def var_definition(self):
        pass

    def expression_statement(self):
        pass

    def no_op(self):
        pass

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
