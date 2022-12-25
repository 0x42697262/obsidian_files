 > [!INFO]
> Status: #WIP
> Tags: #Machine_Problem #CMSC142 #Python

----
# CMSC 142 May the for be with you - version 1
Source Code: https://github.com/KrulYuno/obsidian_files/blob/master/Codes/may_the_for_be_with_you_v1.py
Some references:
- https://github.com/Esamanoaz/plox
- https://craftinginterpreters.com

# TODOs 
- [ ] Write Unit Tests (i swear, it makes your life easier)
- [x] Tokens
- [x] Lexer
	- [x] Scanner
- [ ] Parser (dont think we need this since we only need to assume input source code is correct. no need for abstract syntax trees hehe)


---

# main function
```python
def main():
    lines = int(input())
    source_code = list()
    for _ in range(lines):
        source_code.append(input())

if __name__ == "__main__":
    main()
```
Take number of lines for the code then get each line of the source. Append it to an array list of line by line source code.

Example Input:
```c++
5
int x = 10, y = 8, z = -2;
x = x + y;
y = x - y;
x = x - y;
z = x + y;
```

Example Output:
```python
[
	'int x = 10, y = 8, z = -2;', 
	'x = x + y;', 
	'y = x - y;', 
	'x = x - y;', 
	'z = x + y;'
]
```
This code does not necessarily have an output of array. This is simply for visualization.

Tokens... Ever changing tokens, gets added when needed. Don't know what enums are? Check here: https://docs.python.org/3/library/enum.html because I don't know either (only knew about it in rust sooooo)
```python
from enum import Enum, auto

class TokenType(Enum):
    # single character tokens 
    OPEN_PAREN          = auto() # (
	CLOSE_PAREN         = auto() # )
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
```

So far I do not know what this is for. Probs printing the tokens.
```python
class Token:
    def __init__(self, _type, lexeme, literal, line) -> None:
       self.type    = _type
       self.lexeme  = lexeme
       self.literal = literal
       self.line    = line

    def __str__(self):
        return f"Token<{self.type} : {self.lexeme}, {self.literal}> ({self.line})"
```
# Scanning the input or source
I base my interpreter for C++ here: https://craftinginterpreters.com/scanning.html but used someone's code instead. I can't read Java.
```python
class Scanner:
    def __init__(self, source: str) -> None:
        self.source     = source
        self.tokens     = list()
        self.start      = 0
        self.current    = 0
        self.line       = 1
        self.alpha      = ['_']                                             # [a-zA-Z_]
        self.digits     = [chr(c) for c in range(48, 58)]                   # [0-9]
        for _ in [chr(c) for c in range(97, 123)]:
                self.alpha.append(_)
        for _ in [chr(c) for c in range(65, 91)]:
                self.alpha.append(_)
    ...
```
`start` and `current` are indexes of the string. `start` first character index of a lexeme. `current` current character index. `line` current line of source code (which is the array).
Continuation on the next block of code

Dictionary of token types. [Lambdas](https://docs.python.org/3/reference/expressions.html#lambda), makes life a bit easier. 
```python
...

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
```

Helper functions for character checking the next character of the source input.
```python
...
def _peek(self):
	if self.is_eof():
		return "\0"
	return self.source[self.current]

def _peek_next(self):
	if self.current + 1 >= len(self.source):
		return "\0"
	return self.source[self.current + 1]

def is_digit(self, c):
	return c in self.digits

def is_alpha(self, c):
	return c in self.alpha

def is_alphanum(self, c):
	return self.is_alpha(c) or self.is_digit(c)

def is_eof(self):
	return self.current >= len(self.source)
...
```

Same as above but helper functions for consuming the next character.
```python
...
def _advance(self):
	self.current += 1
	return self.source[self.current - 1]

def _add_token(self, token_type, literal = None):
	text = self.source[self.start : self.current]
	self.tokens.append(Token(token_type, text, literal, self.line))

def _advance_line(self):
	self.line += 1
...
```


Matches an expected character.
```python
...
def _match(self, expected) -> bool:
	if self.is_eof():
		return False
	elif self.source[self.current] != expected:
		return False
	else:
		self.current +=1
		return True
...
```

Loops the source input for characters (or lexemes) then append its token to `self.tokens`.
```python
def scan_token(self):
	while not self.is_eof():
		self.start = self.current
		self._scan_token()

	self.tokens.append(Token(TokenType.EOF, '', None, self.line))
	return self.tokens

def _scan_token(self):
	c = self._advance()
	if c in self.token_strings:
		c = self.token_strings[c](c)
		if c is not None:
			self._add_token(c)
	elif self.is_digit(c):
		self._number_logic()
	elif self.is_alpha(c):
		self._identifier_logic()
	else:
		print(f"Unexpected character on line {self.line}")
```

Helper functions in lexemizing literals and identifiers.

i still dont get how this work
```python
def _string_logic(self):
	starting_line = self.line
	while self._peek() != '\'' and not self.is_eof():
		self._advance()
	
	if self.is_eof():
		print(f"Expected ' at end of string on line {starting_line}")
		return None

	self._advance()
	self._add_token(TokenType.STRING, self.source[self.start+1 : self.current-1])
```
The while loop takes the literal of a string (but in c++, there's only chars so only 1 length) then the last `self._advance()` simply takes the last `'` char. Which then adds a token type string. It starts at `self.start+1` because there is a need to skip the first `'` and `self.current-1` to ignore the last `'`.

Takes number
```python
    def _number_logic(self):
        while self.is_digit(self._peek()):
            self._advance()
        if self._peek() == '.' and self.is_digit(self._peek_next()):
            self._advance()
            while self.is_digit(self._peek()):
                self._advance()
        self._add_token(TokenType.NUMBER, float(self.source[self.start : self.current]))
```
Scans the input token from the starting string till end. Returns float of the token as number.






# BELOW THIS IS OLD NOTES. NOT NEEDED (for archive purpose)

### TODO:
- [ ] Finish Lexer
	- [x] Statement
	- [x] Compound Statement
	- [ ] Conditional Statement 
		- [x] if
		- [ ] else
	- [ ] Loop Statement
		- [ ] for (we only need this)
		- [ ] while
	- [ ] Return Statement (probably dont need it)
	- [x] Variable Definition
	- [x] Expression Statement
	- [x] No-op Statement
	- [ ] Expression
		- [x] Arithmetic
- [ ] Parser (do we need this? maybe we can skip it since there's no need to check for the correct grammar)
- [ ] Counter for T(n)
	- [ ] Count the operators, loops, increments, etc
	- [ ] sum them
	- [ ] decision tree for if-else
	- [ ] Total T(n)

---

regex, ofc ( i don't think this is ever used lol )
```python
import re
```

Token Types
```python
TOKEN_TYPE = {
        '{'     :  'OPEN_BRACE',
        '}'     :  'CLOSE_BRACE',
        '('     :  'OPEN_PAREN',
        ')'     :  'CLOSE_PAREN',
        'if'    :  'KEYWORD',
        'else'  :  'KEYWORD',
        'for'   :  'KEYWORD',
        'int'   :  'DATA_TYPE',
        'float' :  'DATA_TYPE',
        'char'  :  'DATA_TYPE',
        'void'  :  'DATA_TYPE',
        'bool'  :  'DATA_TYPE',
        'var'   :  'IDENTIFIER',
        '='     :  'ASSIGN',
        ';'     :  'SEMICOLON',
        ','     :  'COMMA',
        }
```

For checking if the variable name is allowed. Note that it does not care if a number starts at the beginning. A list of allowed characters.
```python
identifier_chars = ['_']
for c in range(48, 58):
        identifier_chars.append(chr(c))
for c in range(65, 91):
        identifier_chars.append(chr(c))
for c in range(97, 123):
        identifier_chars.append(chr(c))
```
Check [ASCII](https://www.ieee.li/computer/ascii.htm) on why i used those number range.

I needed to tokenize them so that T(n) can easily be counted. *As it should be, right?*
```python
class Lexer:
    def __init__(self, expr: str) -> None:
        self.expr = expr
        self.tokens = list()

        self.cursor = -1
```

These functions should be self-explanatory, right?
```python
...
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
...
```

I then based the recursive-descent parser ( i think? ) on: https://github.com/bisqwit/compiler_series/tree/master/ep1
![Statement Grammar](https://raw.githubusercontent.com/bisqwit/compiler_series/master/ep1/jit-conj-parser1.png)


---
IGNORE WHAT'S BELOW HERE (THIS IS OLD ASF):

~~what to put here soon for future notes... ofc the code~~

```python
def main():
    lines = int(input())
    expression = str()
    for _ in range(lines):
        expression += input()
```

Input Example:
```c++
3
if (x<4){
	x++;
}
```

Output:
```c++
if (x<4){    x++;}
```
We need to parse this.

# BNF Grammar?
```bnf
<expression>  ::=  <type><variable>
<variable>    ::=  <identifier><assignment><_next>
<assignment>  ::=  =<value> | ε
<_next>       ::=  ; | ,<variable>
<type>        ::=  int | float | char | string | bool | void
<identifier>  ::=  [a-zA-Z] [a-zA-Z0-9_]*
<value>       ::= <arithmetic_expression>
```
Source for `<identifier>`: https://mc-stan.org/docs/2_22/reference-manual/bnf-grammars.html

This should read simple statements like:
```c++
int x = 10, y = 8, z = -2;
x = x + y; 
```

Do we really need to tokenize it properly? What if just take the string input up until `;`? Then count the T(n)'s? Since we assume that the input is correct.
In this case take this expression and consume the first `;`:
```c++
int x = 10, y = 8, z = -2;x = x + y;y = x - y;x = x - y;z = x + y;
```
`int x = 10, y = 8, z = -2;` T(n) = 3
`x = x + y;` T(n) = 2
`y = x - y;` T(n) = 2
`x = x - y;` T(n) = 2
`z = x + y;` T(n) = 2

T(n) = 11

As for the `for-loop`, maybe a different approach would be needed. Like, check the keyword `for`, then `statement`, then the scope `{}`, and even include if `else` if the `if-else` exist.

```rust
for(int i=0; i<n; i++){
sum += i;
}
```
If splitting it by `;`, then the result would be `['for(int i=0', ' i<n', ' i++){sum += i', '}']`.

This looks annoying so parse it line by line instead. Just like how it's intended...

Back to Lexer-Parser :D
	