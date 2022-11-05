"""
Grammar:
    <expr>   ::= <term><expr_>
    <expr_>  ::= +<term><expr_> | -<term><expr_> | ε
    <term>   ::= <factor><term_>
    <term_>  ::= *<factor><term_> | /<factor><term_> | ε
    <factor> ::= (<expr>) |<digit>  
    <digit>  ::= 0|1|2|3
"""

"""
        ==========================TOKENS==========================
"""
TokenType = {
                1: "DIGIT",
                2: "OPEN_PAREN",
                3: "CLOSE_PAREN",
                4: "MUL_OP",
                5: "DIV_OP",
                6: "SUB_OP",
                7: "ADD_OP",
                0: "END_INPUT",
                -1: "ILLEGAL"
}

Token_Operators = list()
Token_Operators.append(TokenType[4])
Token_Operators.append(TokenType[5])
Token_Operators.append(TokenType[6])
Token_Operators.append(TokenType[7])
"""
        ========================END TOKENS========================
"""

def is_digit(c) -> bool:
    return True if ord(c) >= 49 and ord(c) <= 51 else False

"""
        =====================LEXICAL ANALYZER=====================
"""
class Lexer:
    def __init__(self, input, pos = 0, read_pos = 0, c = '') -> None:
         self.input = input
         self.pos = pos
         self.read_pos = read_pos
         self.c = c

    def read_char(self) -> None:
        if self.read_pos < len(self.input):
                self.c = self.input[self.read_pos]
        self.pos = self.read_pos
        self.read_pos = self.read_pos + 1

    def next_token(self) -> str:
        token:str = None
        match self.c:
            case '(':
                token = TokenType[2]
            case ')':
                token = TokenType[3]
            case '*':
                token = TokenType[4]
            case '/':
                token = TokenType[5]
            case '-':
                token = TokenType[6]
            case '+':
                token = TokenType[7]
            case '$':
                token = TokenType[0]
            case _:
                if is_digit(self.c):
                    token = TokenType[1]
                else:
                    token = TokenType[-1]
        self.read_char()
        return token
"""
        =====================LEXICAL ANALYZER=====================
"""

"""
        ==========================PARSER==========================
"""
class Parser:
    def __init__(self) -> None:
        self.input = str()
        self.paren_count = 0
        self.tokens = list()

    def parse(self, input) -> bool:
        self.input = input
        self.paren_count = 0
        self.tokens = list()
        self.build_tokens()

        return self.expr()

    def build_tokens(self) -> None:
        Lex = Lexer(self.input)
        Lex.read_char()
        for _ in self.input:
            self.tokens.append(Lex.next_token())

    def consume(self) -> str:
        if len(self.tokens) > 0:
            return self.tokens.pop(0)
        return None

    def eof(self) -> bool:
        return True

    def illegal(self) -> bool:
        return False

    def expr(self) -> bool:
        token = self.consume()
        result = None
        
        if token == TokenType[1]:
            result = self.digit()

        elif token == TokenType[2]:
            result = self.open_paren()

        else:
            result = self.illegal()

        if self.paren_count != 0:
            return False
        
        if result == True:
            return True if (len(self.tokens) == 0) else False

        return result
        
    
    def digit(self) -> bool:
        token = self.consume()
        if token in Token_Operators:
            return self.operator()
            
        elif token == TokenType[0]:
            return self.eof()

        elif token == TokenType[3]:
            return self.close_paren()

        else:
            return self.illegal()

    def operator(self) -> bool:
        token = self.consume()
        if token == TokenType[1]:
            return self.digit()
        
        elif token == TokenType[2]:
            return self.open_paren()

        else:
            return self.illegal()
    
    def open_paren(self) -> bool:
        self.paren_count = self.paren_count + 1       
        token = self.consume()
        if token == TokenType[1]:
            return self.digit()

        if token == TokenType[2]:
            return self.open_paren()

        else:
            return self.illegal()

    def close_paren(self) -> bool:
        self.paren_count = self.paren_count - 1
        token = self.consume()
        if token == TokenType[0]:
            return self.eof()
        
        elif token == TokenType[3]:
            return self.close_paren()

        elif token in Token_Operators:
            return self.operator()

        else:
            return self.illegal()

            
"""
        =========================END PARSER=========================
"""

def main():
    par = Parser()
    print(par.parse("(((1*1*1*1*1-1-2-3-1/1/1*1+1)))$"))


if __name__ == "__main__":
    main()
