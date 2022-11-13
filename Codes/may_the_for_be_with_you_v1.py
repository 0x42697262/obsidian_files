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
        # FORGIVE JESUS CHRIST FOR THIS SPAGHETTI CODE
        if self.peek() == 'f' and self.peek(2) == 'o' and self.peek(3) == 'r':
                self.insert_token(TOKEN_TYPE['for'])
                self.next(3)

                if self.peek() == '(':
                    self.insert_token(TOKEN_TYPE['('])
                    self.next()
                    # for(int i=0; i<n; i++)
                    
                    # int part: int
                    while self.peek() in [chr(c) for c in range(97, 123)]:
                        self.insert_token(TOKEN_TYPE['lit'])
                        self.next()

                    # identifier part: i
                    while self.peek() in [chr(c) for c in range(97, 123)]:
                        self.insert_token(TOKEN_TYPE['var'])
                        self.next()

                    # assign: =
                    if self.peek() == '=':
                        self.insert_token(TOKEN_TYPE['='])
                        self.next()
            
                    # literal: 0 
                    while self.peek() in literal_chars or self.peek == ';':
                        self.insert_token(TOKEN_TYPE['lit'])
                        self.next()
                    print(f"{self.expr[self.cursor]} --> {self.peek()} AHHHH")

                    # semicolon: ;
                    if self.peek() == ';':
                        self.insert_token(TOKEN_TYPE[';'])
                        self.next()
                    print(f"{self.expr[self.cursor]} --> {self.peek()}")

                    # identifier: i
                    while self.peek() in [chr(c) for c in range(97, 123)]:
                        self.insert_token(TOKEN_TYPE['var'])
                        self.next()
                    print(f"{self.expr[self.cursor]} --> {self.peek()}")

                    # condition operation: <
                    if self.peek() in ['<', '>', '<=', '>=', '==', '!=']:
                        self.insert_token("OPERATION")
                        self.next()
                    print(f"{self.expr[self.cursor]} --> {self.peek()}")

                    # identifier: n
                    while self.peek() in [chr(c) for c in range(97, 123)]:
                        self.insert_token(TOKEN_TYPE['var'])
                        self.next()
                    print(f"{self.expr[self.cursor]} --> {self.peek()}")

                    # semicolon: ;
                    if self.peek() == ';':
                        self.insert_token(TOKEN_TYPE[';'])
                        self.next()
                    print(f"{self.expr[self.cursor]} --> {self.peek()}")
                    
                    # increment: i++
                    if (self.peek() == '-' and self.peek(2) == '-') or (self.peek() == '+' and self.peek(2) == '+'):
                        self.insert_token("OPERATION")
                        self.next(2)
                    print(f"{self.expr[self.cursor]} --> {self.peek()}")

                    if self.peek() == ')':
                        self.insert_token(TOKEN_TYPE[')'])
                        self.next()
                        self.statement()

    def return_statement(self):
        pass 

    def var_definition(self):
        # this place got mistakes but whatever, we only need to lex the lexemes anyways
        if self.peek() in identifier_chars:
            while self.peek() in identifier_chars:
                self.cursor += 1

            self.insert_token(TOKEN_TYPE['lit'])
            self.next(0)
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
        l = Lexer(expr)

        while l.peek() is not None:
            l.statement()

        for tokens in l.tokens:
            if tokens in ['ASSIGN', 'OPERATION', 'BITWISE']:
                self.t_n += 1

        print(l.tokens)

    def get_n(self) -> int:
        return self.t_n

class Tokenizer:
    def __init__(self, input_expr) -> None:
        self.tokens = list()
        self.index = 0
        self.input_expr = input_expr

    def peek(self, i=1):
        if self.index + i < len(self.input_expr):
            return self.input_expr[self.index + i]
        return "\\EOF\\"

    def next(self, i=1):
        self.index += i
        self.skip_ws()

    def skip_ws(self):
        while self.peek() == ' ':
            self.index += 1

    def is_data_type(self, i=0) -> bool:
        text = re.findall(r'[a-zA-Z][a-zA-Z]*', self.input_expr[i:])
        
        if len(text):
            if text[0] in ['int', 'char', 'void', 'float', 'bool']:
                self.index += len(text[0]) - 1
                self.next()
                return True
        return False

    def read_identifier(self, i=0):
        text = re.findall(r'[a-zA-Z_][a-zA-Z_0-9]*', self.input_expr[i:])
        
        if len(text):
            self.index += len(text[0]) - 1
            self.next()
            self.tokens.append('IDENTIFIER')


    def statement(self):
        self.var_def_statement()
        self.var_statement()
        
    def var_def_statement(self):
        # type -> iden -> ; 
        #              -> , -> ::
        #              -> = -> arith_expr -> , -> ::
        #                                 -> ;
        if self.is_data_type():
            self.tokens.append("TYPE")
            self.var_def_statement_()

    def var_def_statement_(self):
        self.read_identifier(self.index)
        match self.peek():
            case ';':
                self.tokens.append(';')
                self.next()
            case ',':
                self.tokens.append(',')
                self.next()
                self.var_def_statement_()
            case '=':
                self.tokens.append('=')
                self.next()
                self.expression_statement() 

        if self.peek() == ';':
            self.tokens.append(';')
            self.next()

    def var_statement(self):
        if not self.is_data_type():
            self.read_identifier(self.index)
            if self.input_expr[self.index] != ' ':
                self.index -= 1

            if self.peek() == '=':
                self.tokens.append('=')
                self.next()
                self.expression_statement()

                print(self.peek())
                if self.peek() == ';':
                    self.tokens.append(';')
                    self.next()

    def expression_statement(self):
        # LIT/NUM -> OP -> ::
        text = re.findall(r'-{0,1}\d*\.{0,1}\d+|[a-zA-Z_][a-zA-Z_0-9]*', self.input_expr[self.index::])
        if len(text):
            self.index += len(text[0]) - 1
            self.next()
            self.tokens.append('LITERAL')

            if self.peek() in ['+', '-', '*', '/', '**']:
                self.tokens.append("OP")
                self.next()
                self.expression_statement()


        print(len(text[0]), text)




def main():
    # Take inputs, assume inputs are correct
    # no sanitization
    lines = int(input())
    expression = str()
    for _ in range(lines):
        expression += input()



if __name__ == "__main__":
    main()
