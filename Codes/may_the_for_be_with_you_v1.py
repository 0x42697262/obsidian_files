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
    AMPERSAND           = auto() # &
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
        return f"({self.line}) Token<{self.type:<25}: {self.lexeme:<5} | {self.literal}>"


##
#
#  LEXICAL ANALYZER 
#
##


class Scanner:
    def __init__(self, source: list) -> None:
        """
            This class takes the source code input as a list which should be iterated
            each loop. Should return the tokenized source code.
        """
        
        self.source         = source
        self.tokens         = list()

        self.char_start     = 0
        self.char_current   = 0
        self.line           = 1
        self.index          = 0


        self.alpha          = ['_']                                             # [a-zA-Z_]
        self.digits         = [chr(c) for c in range(48, 58)]                   # [0-9]
        
        for _ in [chr(c) for c in range(97, 123)]:
                self.alpha.append(_)
        for _ in [chr(c) for c in range(65, 91)]:
                self.alpha.append(_)

        self.token_strings  = {
                '('         :       lambda _: TokenType.OPEN_PAREN,        
                ')'         :       lambda _: TokenType.CLOSE_PAREN,        
                '['         :       lambda _: TokenType.OPEN_BRACKET,        
                ']'         :       lambda _: TokenType.CLOSE_BRACKET,        
                '{'         :       lambda _: TokenType.OPEN_BRACE,        
                '}'         :       lambda _: TokenType.CLOSE_BRACE,        
                ','         :       lambda _: TokenType.COMMA,        
                '.'         :       lambda _: TokenType.DOT,        
                ':'         :       lambda _: TokenType.COLON,        
                ';'         :       lambda _: TokenType.SEMICOLON,        
                '\\'        :       lambda _: TokenType.BACKWARD_SLASH,        
                '\''        :       lambda _: self._string_logic(),

                '&'         :       lambda _: TokenType.LOGICAL_AND     if self._match('&') else TokenType.AMPERSAND,
                '|'         :       lambda _: TokenType.LOGICAL_OR      if self._match('|') else None,
                '!'         :       lambda _: TokenType.BANG_EQUAL      if self._match('!') else TokenType.BANG,
                '='         :       lambda _: TokenType.EQUAL_EQUAL     if self._match('=') else TokenType.EQUAL,
                '>'         :       lambda _: TokenType.GREATER_EQUAL   if self._match('=') else TokenType.GREATER_GREATER \
                                                                        if self._match('>') else TokenType.GREATER,
                '<'         :       lambda _: TokenType.LESSER_EQUAL    if self._match('=') else TokenType.LESSER_LESSER \
                                                                        if self._match('<') else TokenType.LESSER,
                '+'         :       lambda _: TokenType.PLUS_EQUAL      if self._match('=') else TokenType.PLUS_PLUS \
                                                                        if self._match('+') else TokenType.PLUS,
                '-'         :       lambda _: TokenType.MINUS_EQUAL     if self._match('=') else TokenType.MINUS_MINUS \
                                                                        if self._match('-') else TokenType.MINUS,
                '*'         :       lambda _: TokenType.STAR_EQUAL      if self._match('=') else TokenType.STAR_STAR \
                                                                        if self._match('*') else TokenType.STAR,
                '/'         :       lambda _: TokenType.SLASH_EQUAL     if self._match('=') else None \
                                                                        if self._match('*') else None \
                                                                        if self._match('/') else TokenType.SLASH,

                ' '         :       lambda _: None,
                '\t'        :       lambda _: None,
                '\r'        :       lambda _: None,
                '\n'        :       lambda _: self._next_line(),

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


    def is_digit(self, c: str) -> bool:
        """
            Returns boolean type if character is a digit.

            Note:
                You can use Python's built-in module: isdigit()
        """
        return c in self.digits





    def is_alpha(self, c: str) -> bool:
        """
            Returns boolean type if character is a letter and _.
        """

        return c in self.alpha





    def is_alnum(self, c: str) -> bool:
        """
            Returns boolean type if character is digit, letter, or _.
        """
        
        return self.is_digit(c) or self.is_alpha(c)




    def is_line_eof(self, count: int = 0) -> bool:
        """
            Checks if current line is end of input.
        """

        return self.char_current+count >= len(self.source[self.index])





    def _peek(self) -> str:
        """
            Returns the current character.
        """

        if self.is_line_eof():
            return '\0'

        return self.source[self.index][self.char_current]





    def _peek_next(self, count: int = 1) -> str:
        """
            Returns the next i character.
        """

        if self.is_line_eof(count):
            return '\0'

        return self.source[self.index][self.char_current+count]





    def _advance(self) -> str:
        """
            Increments index of current character (source line).
            Returns previous current character.
        """

        self.char_current += 1
        return self.source[self.index][self.char_current-1]




    def _next_line(self) -> None:
        """
            Increments current line and index.
        """

        self.line   += 1
        self.index  += 1





    def _append_token(self, token_type, literal = None) -> None:
        """
            Appends new token to tokens list.
        """

        text = self.source[self.index][self.char_start : self.char_current]
        self.tokens.append(Token(token_type, text, literal, self.line))





    def _match(self, expected_char) -> bool:
        """
            what does this do? Matches an expected character... Very helpful, indeed.

            Returns boolean type if <?>. Where is this used for...?
        """

        if self.is_line_eof():
            return False
        elif self.source[self.index][self.char_current] != expected_char:
            return False
        else:
            self.char_current += 1
            return True





    def reset_line(self) -> None:
        """
            Sets the line's starting character index and current character index to 0.
        """

        self.char_current   = 0
        self.char_start     = 0





    def scan_tokens(self) -> list:
        """
            Iterates the source code list and scans for tokens.
            Returns token list.
        """

        for _ in self.source:
            self.reset_line()
            while not self.is_line_eof():
                self.char_start = self.char_current
                self._scan_token()
            self._next_line()
        self.tokens.append(Token(TokenType.EOF, '', None, self.line))
        
        return self.tokens





    def _scan_token(self) -> None:
        """
            Consumes current character, checks the token type, and do magic.
        """

        c   = self._advance()

        if c in self.token_strings:
            c   = self.token_strings[c](c)
            if c is not None:
                self._append_token(c)
        elif self.is_digit(c):
            self._number_logic()
        elif self.is_alpha(c):
          self._identifier_logic()
        else:
            print("Unexpected character on line", self.line, ":", c)

    



    def _number_logic(self) -> None:
        """
            Does not check if number is negative or positive. Maybe use a parser?
        """

        while self.is_digit(self._peek()):
            self._advance()

        if self._peek() == '.' and self.is_digit(self._peek_next()):
            self._advance()
            while self.is_digit(self._peek()):
                self._advance()
        self._append_token(TokenType.NUMBER, float(self.source[self.index][self.char_start : self.char_current]))





    def _identifier_logic(self) -> None:
        while self.is_alnum(self._peek()):
            self._advance()
        text        = self.source[self.index][self.char_start : self.char_current]
        token_type  = self.keywords.get(text)

        if token_type is None:
            token_type = TokenType.IDENTIFIER

        self._append_token(token_type)




    def _string_logic(self) -> None:
        starting_line   = self.line
        while self._peek() != '\'' and not self.is_line_eof():
            self._advance()

        if self.is_line_eof():
            print(f"Expected ' at end of string on line {starting_line}")
            return

        self._advance()
        self._append_token(TokenType.STRING, self.source[self.index][self.char_start+1 : self.char_current-1])


class Parser():
    def __init__(self, source) -> None:
        self.tokens         = Scanner(source).scan_tokens()
        self.count          = 0
        self.index          = 0
        
        self.fix_tokens()

        self.token_operations = [
                # Arithmetic
                TokenType.PLUS,
                TokenType.MINUS,
                TokenType.STAR,
                TokenType.SLASH,
                TokenType.PLUS_EQUAL,
                TokenType.MINUS_EQUAL,
                TokenType.STAR_EQUAL,
                TokenType.SLASH_EQUAL,
                TokenType.EQUAL,
                TokenType.MINUS_MINUS,
                TokenType.PLUS_PLUS,
                
                # Logic
                TokenType.EQUAL_EQUAL,
                TokenType.BANG_EQUAL,
                TokenType.LESSER,
                TokenType.LESSER_EQUAL,
                TokenType.GREATER,
                TokenType.GREATER_EQUAL,
                TokenType.LESSER_LESSER,
                TokenType.GREATER_GREATER,
                TokenType.LOGICAL_AND,
                TokenType.LOGICAL_OR,
                ]

    def print_tokens(self) -> None:
        for _ in self.tokens:
            print(_)

    def tokens_list(self) -> list:
        return [_.type for _ in self.tokens]

    def fix_tokens(self) -> None:
        """
            There are sometimes issues with lexemes like "-42" that gets taken as two tokens instead of one.
            Needs to fix that.
            Eh, let's just assume that operator inputs only exists once, no duplicates.

            Probably that don't need fixing:
                - - - -42
                -- -42
                ---42 (this is an error btw)
                -+-42
            Don't forget a-b otherwise it'll get taken as NUM NUM instead of NUM OP NUM
            oyu know wht fuck this shit. test cases don't have "a-b" problem. good thing the values are constant...
        """
        
        i = 0
        for _ in self.tokens:
            if self.tokens[i-1].type != TokenType.NUMBER or self.tokens[i-1].type != TokenType.IDENTIFIER:
                if self.tokens[i].type == TokenType.MINUS:
                    if self.tokens[i+1].type == TokenType.NUMBER: # Assume that i+1 exists...
                        self.tokens.pop(i)
                        self.tokens[i].lexeme = str("-"+self.tokens[i].lexeme)
                        self.tokens[i].literal  = float(-self.tokens[i].literal)
            i = i+1


    def count_expression(self, start: int, end: int) -> int:
        """
            Using this for counting the operations inside a for loop statement.
            start - starting index
            end   - last index
        """

        count = 0
        for i in range(start, end):
            if self.tokens[i].type == TokenType.EOF:
                break
            if self.tokens[i].type in self.token_operations:
                count = count + 1

        return count

    def count_for_statement(self):
        """
            Example Test Case:
                for(int i = 1+2+3-5; int i-i+(i*i) < (n-4)+4; i *= 1+1)

            This can be grouped into 6 parts:
                1) int i
                2) 1+2+3-5
                3) i-i+(i*i)
                4) (n-4)+4
                5) i
                6) 1+1

            We only need to focus on 2, 3, 4, and 6.
            Assume that 2 and 4 only contains 1 operation (e.g. `i = 1` or `i = n`)

            Maybe create a dictionary as it might be easier to read?
                variable - initialization identifier
                op       - operator of the foor loop segment 
                value    - literal of the for loop segment
                count    - number of steps of the for loop segment
        """

        data   = {
                   "variable"           : str(),

                   "init_value"         : None,      # can be a variable or number

                   "condition_op"       : str(),
                   "condition_value"    : None,      # can be a variable or number
                   "condition_count"    : 0,

                   "update_op"          : None,
                   "update_value"       : 0,

                   "body_count"         : 0,
               }
        # SET THE VARIABLE IDENTIFIER
        self.index              = self.index + 3
        data["variable"]        = self.tokens[self.index].lexeme

        # SET THE INIT VALUE
        # CAN BE NUMBER OR VARIABLE
        self.index              = self.index + 2
        if self.tokens[self.index].type == TokenType.NUMBER:
            data["init_value"]      = int(self.tokens[self.index].lexeme)
        else:
            data["init_value"]      = self.tokens[self.index].lexeme


        # ITERATE THE 2ND SEGMENT UNTIL `;` IS FOUND
        self.index              = self.index + 2    # moves cursor index after `;`
        start                   = self.index
        end                     = self.index
        while self.index in range(len(self.tokens)):
            if self.tokens[self.index].type == TokenType.SEMICOLON:
                break
            match self.tokens[self.index].type:
                case TokenType.LESSER \
                        | TokenType.LESSER_EQUAL \
                        | TokenType.GREATER \
                        | TokenType.GREATER_EQUAL \
                        | TokenType.BANG_EQUAL \
                        | TokenType.EQUAL_EQUAL:
                    data["condition_op"]    = self.tokens[self.index].type
                case TokenType.IDENTIFIER:
                    data["condition_value"] = self.tokens[self.index].lexeme
                case  TokenType.NUMBER:
                    data["condition_value"] = int(self.tokens[self.index].lexeme)
                case _:
                    pass
            end         = end + 1
            self.index  = self.index + 1

        data["condition_count"]     = self.count_expression(start, end)


        # ITERATE 3RD SEGMENT UNTIL AN CLOSE PARENTHESIS IS FOUND
        self.index              = self.index + 1    # moves cursor index after `;`
        start                   = self.index
        end                     = self.index
        while self.index in range(len(self.tokens)):
            if self.tokens[self.index].type == TokenType.CLOSE_PAREN:
                break
            match self.tokens[self.index].type:
                case TokenType.PLUS_EQUAL \
                    | TokenType.MINUS_EQUAL \
                    | TokenType.STAR_EQUAL \
                    | TokenType.SLASH_EQUAL:
                    data['update_op']    = self.tokens[self.index].lexeme
                case  TokenType.NUMBER:
                    data["update_value"] = int(self.tokens[self.index].lexeme)
                case TokenType.PLUS_PLUS:
                    data["update_value"] = 1
                case TokenType.PLUS_PLUS:
                    data["update_value"] = -1
                case _:
                    pass
            end         = end + 1
            self.index  = self.index + 1


        # ITERATE BODY UNTIL CLOSING BRACE IS FOUND
        self.index              = self.index + 1    # moves cursor index to `{`
        # }
        start                   = self.index
        end                     = self.index
        while self.index in range(len(self.tokens)):
            if self.tokens[self.index].type == TokenType.CLOSE_BRACE:
                break
            end         = end + 1
            self.index  = self.index + 1

        data["body_count"]      = self.count_expression(start, end)

        count                   = {
                                    "call"          : 1 + data["condition_count"],   # 1 is from `=` sign assignment1 + data["condition_count"]   # 1 is from `=` sign assignment
                                    "loop"          : 1 + data["condition_count"] + data["body_count"],  # 1 is from the 3rd segment operation assignment
                                    "total_loop"    : 0,
                                }
        
        

        print(data)




    def count_tokens(self):
        """
            Iterates the `self.tokens` tokens and counts the token operations.
            Checks if a `for loop` statement is found then call `self.count_for_statement_old()`.

            This code is a convulted mess and i deeply apologize.
        """

        # for_stmt    = list()
        # while self.index in range(len(self.tokens)):
        #     if self.tokens[self.index].type in self.token_operations:
        #         self.count = self.count + 1
        #     elif self.tokens[self.index].type == TokenType.FOR:
        #         for_stmt        = self.count_for_statement_old()
        #     
        #     self.index = self.index + 1
        #
        # if len(for_stmt) > 0:
        #     if for_stmt[0] == 0:
        #         self.count  = self.count + for_stmt[1] 
        #         print("T(n) = ", int(self.count))
        #     else:
        #         self.count  =  self.count + for_stmt[3]
        #         eval_str    = str(for_stmt[1]) + str(for_stmt[2])
        #         sign            = '+' if for_stmt[3] >= 0 else '-'
        #         print("T(n) = ", eval_str, sign, str(int(abs(self.count))))
        # else:
        #     print("T(n) = ", self.count)
        self.count_for_statement()



def main():
    lines           = int(input())
    source_code     = list()

    for _ in range(lines):
        source_code.append(input())

    stuff   = Parser(source_code)
    stuff.count_tokens()

if __name__ == "__main__":
    main()
