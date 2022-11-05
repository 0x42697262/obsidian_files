> [!INFO]
> Status: #WIP
> Tags: #CMSC124 #Machine_Problem 

----
# CMSC 124 Machine Problem 3 Documentation

Implement a **recursive-descent parser** for the following grammar rules:

### 1. Grammar rules for an arithmetic expression:
```
<expr>   ::= <expr>+<term> | <expr>-<term> | <term>  
<term>   ::= <term>*<factor> | <term>/<factor> | <factor>  
<factor> ::= (<expr>) |<digit>  
<digit>  ::= 0|1|2|3
```
Terminate every input string with `‘$’`.

| Valid Input String Examples: | Invalid Input String Examples: |
| ---------------------------- | ------------------------------ |
| 1-2\*3$                      | 22-3$                          |
| (1-2)\*(3+1)$                | (4-1)\*3$                      |
| 2/3$                         | 3/$                            |

### 2. Grammar rules for a multi-digit decimal number
```
<expr>   ::= +<num> | -<num> | <num>  
<num>    ::= <num><digits> | <digits>  
<digits> ::= <digit> | <digit>.<digit>  
<digit>  ::= 0|1|2|3|4|5|6|7|8|9
```
Terminate every input string with `‘$’`.

| Valid Input String Examples: | Invalid Input String Examples: |
| ---------------------------- | ------------------------------ |
| 6$                           | 5.55.55$                       |
| -15.5$                       | a33$                           |
| +9.99$                       | ++22.20$                       |
| 33.369$                      | -5.4.2$                        |

---

### Rewriting the grammars
The first grammar is left recursive and left factored, the non-terminals `<expr>` and `term` can be rewritten to:
```
<expr>   ::= <term><expr_>
<expr_>  ::= +<term><expr_> | -<term><expr_> | ε

<term>   ::= <factor><term_>
<term_>  ::= *<factor><term_> | /<factor><term_> | ε
```
So, the new grammar is now:
```
<expr>   ::= <term><expr_>
<expr_>  ::= +<term><expr_> | -<term><expr_> | ε
<term>   ::= <factor><term_>
<term_>  ::= *<factor><term_> | /<factor><term_> | ε
<factor> ::= (<expr>) |<digit>  
<digit>  ::= 0|1|2|3
```

The second grammar needs to be written as it accepts the input `5.55.55` which should be an invalid string
```
<num><digits>
<num><digits><digits>
<num><digits><digits>
<num><digit>.<digit><digits>
<num><digit>.<digit><digits>
<num><digits><digit>.<digit><digits>
<digit>.<digit><digit>.<digit><digit>
5.55.55
```
The new grammar would be:
```
<expr>    ::= +<num> | -<num> | <num>  
<num>     ::= <int> | <int>.<int>
<int>     ::= <digit><int_>
<int_>    ::= <int> | ε
<digit>   ::= 0|1|2|3|4|5|6|7|8|9
```

Both grammars now satisfy:
1. Free from left recursion
2. It is now left factored

### Coding the arithmetic expression grammar
In building the lexer, I started listing the token kinds or types for the grammar first. This is needed for the lexer to identify the type of tokens.
```python
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
```
There is no need to include the values of the tokens since we are only parsing if the input string is correct based on the grammar.
`Token_Operators` is group of operators.

This function checks if the character of the input string is `1`, `2`, or `3` based on the grammar.
```python
def is_digit(c) -> bool:
    return True if ord(c) >= 49 and ord(c) <= 51 else False
```
We can use `int()` to convert the character into integer then check it from there. However, only numbers can be converted and other characters would result a `ValueError` like the operators. `ord()` is used since we can base it on the ASCII table as decimal. See [IEEE standards](https://www.ieee.li/computer/ascii.htm).

Class `Lexer` is divided into 3 methods: the initialization, reading of character, and converting a token.
```python
class Lexer:
    def __init__(self, input, pos = 0, read_pos = 0, c = '') -> None:
		...
		
    def read_char(self) -> None:
        ...

    def next_token(self) -> str:
        ...
```

`__init__()` function takes an input string of expression and sets the class variables. Returns nothing.
```python
...
 def __init__(self, input, pos = 0, read_pos = 0, c = '') -> None:
         self.input = input
         self.pos = pos
         self.read_pos = read_pos
         self.c = c
```
There is no need to include `pos`, `read_pos`, and `c` in the argument but I left it as is just in case.
`self.input` expression string input.
`self.pos` current character position of the input.
`self.read_pos` next character position of the input.
`self.c` current character of the input.

`read_char()` increments `self.pos` and `self.read_pos` then sets the character `self.c`.
```python
...
def read_char(self) -> None:
	if self.read_pos < len(self.input):
			self.c = self.input[self.read_pos]
	self.pos = self.read_pos
	self.read_pos = self.read_pos + 1
```
This function is used by `next_token()` function to scan the next character of the expression input.

`next_token()` scans the current character then sets and return its `TokenType`. This function should be ran inside a loop.
```python
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
```
I strictly follow the grammar rules so whitespaces are not ignored but instead considered as an invalid input.
Python does not have switch statements but in Python 3.10, match exists which is similar to switch. See [PEP 636 – Structural Pattern Matching](https://peps.python.org/pep-0636/).


### Coding the multi-digit decimal grammar

A class `Parser` that checks if the expression is grammatically correct based on the tokens provided by the lexer `Lexer`.
```python
class Parser:
    def __init__(self, input: str) -> None:
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
        ...

    def digit(self) -> bool:
        ...

    def operator(self) -> bool:
        ...
    
    def open_paren(self) -> bool:
        ...

    def close_paren(self) -> bool:
        ...
```
`__init__()` function initializes the class parser.
- `self.input` input string expression
- `self.paren_count` used for checking parenthesis grammar. Tallies `(`.
- `self.tokens` list of token types based on characters of the expression.
`parse()` function takes input string expression then returns `True` or `False` if the given expression is correct.
`build_tokens()` creates a class object for the lexer and scans each character expression into token types. Notice that `Lexer.next_token()` function is looped.
`consume()` function pops the first index of the list of tokens `self.tokens` and returns a token type.
`eof()` end of the input string expression `$`, returns `True`.
`illegal()` returns `False` when illegal token `TokenType[-1]` is found.

`expr()` function takes and removes the first element of the index tokens `self.tokens` then starts the recursive-descent parser. Returns a boolean if the expression is correct based on the grammar definition.
```python
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
```
First checks if the token is a digit or an open parenthesis then proceeds to the next token. `self.paren_count` is used here to determine whether open and close parenthesis are of equal amount, and would return false if they are not.
If `$` is found, it checks if it is the last character then returns `True` if it is otherwise `False` because the grammar is incorrect.

The main recursion process of the parser that checks whether the tokens are in the right order.
```python
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
```

### How To Use?
Create a parser object then input the expression in the `parse()` function as this returns a boolean if the expression is correct or not.
```python
par = Parser()
print(par.parse("1+2*3$"))
```
Or use a [test unit](https://github.com/KrulYuno/obsidian_files/blob/master/Codes/test_mp3_recursive_descent_parser_1.py) for validating inputs.

Source Code for \#1: https://github.com/KrulYuno/obsidian_files/blob/master/Codes/mp3_recursive_descent_parser_1.py

---
I was able to write the code for this machine problem thanks to [mohitk05's repository](https://github.com/mohitk05/monkey-rust) and a little reading of this [page](https://michael-f-bryan.github.io/static-analyser-in-rust/book/lex.html) about writing static analyzer for rust.

---
### Sources
- https://mohitkarekar.com/posts/pl/lexer/
- https://michael-f-bryan.github.io/static-analyser-in-rust/book/lex.html