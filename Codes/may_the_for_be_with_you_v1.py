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
            self.insert_token(TOKEN_TYPE['{'])
            self.next()
            self.statement()

            if self.peek() == '}':
                self.insert_token(TOKEN_TYPE['}'])
                self.next()
       
    def conditional_statement(self):
        if self.peek() == 'i' and self.peek(2) == 'f':
            self.insert_token(TOKEN_TYPE['if'])
            self.next(2)
            if self.peek() == '(':
                self.insert_token(TOKEN_TYPE['('])
                self.next()
                self.expression()

                if self.peek() == ')':
                    self.insert_token(TOKEN_TYPE[')'])
                    self.next()
                    self.statement()
    
    def for_loop(self):
        if self.peek() == 'f' and self.peek(2) == 'o' and self.peek(3) == 'r':
                self.insert_token(TOKEN_TYPE['for'])
                self.next(3)

                if self.peek() == '(':
                    self.insert_token(TOKEN_TYPE['('])
                    self.next()
                    self.expression()

                    if self.peek() == ')':
                        self.insert_token(TOKEN_TYPE[')'])
                        self.next()
                        self.statement()

    def return_statement(self):
        pass 

    def var_definition(self):
        if self.peek() == 'i' and self.peek(2) == 'n' and self.peek(3) == 't':
                self.insert_token(TOKEN_TYPE['int'])
                self.next(3)
                self.read_identifier()
        elif self.peek() == 'c' and self.peek(2) == 'h' and self.peek(3) == 'a' and self.peek(4) == 'r':
                self.insert_token(TOKEN_TYPE['char'])
                self.next(4)
                self.read_identifier()
        elif self.peek() == 'f' and self.peek(2) == 'l' and self.peek(3) == 'o' and self.peek(4) == 'a' and self.peek(5) == 't':
                self.insert_token(TOKEN_TYPE['float'])
                self.next(5)
                self.read_identifier()
        elif self.peek() == 'v' and self.peek(2) == 'o' and self.peek(3) == 'i' and self.peek(4) == 'd':
                self.insert_token(TOKEN_TYPE['void'])
                self.next(4)
                self.read_identifier()
        elif self.peek() == 'b' and self.peek(2) == 'o' and self.peek(3) == 'o' and self.peek(4) == 'l':
                self.insert_token(TOKEN_TYPE['bool'])
                self.next(4)
                self.read_identifier()

                

    def expression_statement(self):
        self.expression()
        
        if self.peek() == ';':
            self.insert_token(TOKEN_TYPE[';'])
            self.next()

    def no_op(self):
        if self.peek() == ';':
            self.insert_token(TOKEN_TYPE[';'])
            self.next()

    def read_identifier(self):
        while self.peek() in identifier_chars:
            self.cursor += 1

        self.insert_token(TOKEN_TYPE['var'])
        self.next(0)
        match self.peek():
            case ';':
                self.insert_token(TOKEN_TYPE[';'])
                self.next()

            case '=':
                self.insert_token(TOKEN_TYPE['='])
                self.next()
                self.expression()
                
                if self.peek() == ',':
                    self.insert_token(TOKEN_TYPE[','])
                    self.next()
                    self.read_identifier()

            case ',':
                self.insert_token(TOKEN_TYPE[','])
                self.next()
                self.read_identifier()
        
    def expression(self):
        self.literal_expression()
        self.grouped_expression()

    def literal_expression(self):
        if self.peek() == '-':
            self.next()

        if self.peek() in identifier_chars  or self.peek() in literal_chars:
            while self.peek() in identifier_chars or self.peek() in literal_chars:
                self.cursor += 1
            
            self.insert_token(TOKEN_TYPE['lit'])
            self.next(0)
            self.arithmetic_expression()

    def grouped_expression(self):
        if self.peek() == '(':
            self.insert_token(TOKEN_TYPE['('])
            self.next()
            self.expression()

            if self.peek() == ')':
                self.insert_token(TOKEN_TYPE[')'])
                self.next()

    def arithmetic_expression(self):
        if self.peek() in ['+', '-', '*', '/']:
            self.insert_token("OPERATION")
            self.next()
            self.expression()

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

    while l.peek() is not None:
        l.statement()
    
    print(l.tokens)

if __name__ == "__main__":
    main()
