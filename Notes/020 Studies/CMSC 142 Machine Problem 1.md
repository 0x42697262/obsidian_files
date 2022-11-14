 > [!INFO]
> Status: #WIP
> Tags: #Machine_Problem #CMSC142 #Python

----
# CMSC 142 May the for be with you - version 1
Source Code: https://github.com/KrulYuno/obsidian_files/blob/master/Codes/may_the_for_be_with_you_v1.py

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
```
5
int x = 10, y = 8, z = -2;
x = x + y;
y = x - y;
x = x - y;
z = x + y;
```

Example Output:
```
[
	'int x = 10, y = 8, z = -2;', 
	'x = x + y;', 
	'y = x - y;', 
	'x = x - y;', 
	'z = x + y;'
]
```
This code does not necessarily have an output of array. This is simply for visualization.

# Scanning the input or source
I base my interpreter for C++ here: https://craftinginterpreters.com/scanning.html
```python
class Scanner:
    def __init__(self, source: str) -> None:
        self.source = source
        self.tokens = list()

        self.start = 0
        self.current = 0
        self.line = 1
```
`start` and `current` are indexes of the string.







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
	