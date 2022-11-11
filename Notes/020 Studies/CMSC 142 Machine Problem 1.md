> [!INFO]
> Status: #WIP
> Tags: #Machine_Problem #CMSC142 #Python

----
# CMSC 142 May the for be with you - version 1

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
	- [ ] Variable Definition (WIP right now)
	- [ ] Expression Statement
	- [ ] No-op Statement
	- [ ] Expression
- [ ] Finish Parser (do we need this? maybe we can skip it since there's no need to check for the correct grammar)
- [ ] Finish Counter for T(n)
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
var_name = ['_']
for c in range(48, 58):
        var_name.append(chr(c))
for c in range(65, 91):
        var_name.append(chr(c))
for c in range(97, 123):
        var_name.append(chr(c))
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
        print(f"Token: {token}")
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
	