CMSC 124 Machine Problem 2  
**Topic Coverage**: Syntax and Semantics

### 1. Write a syntactic specification using Backus-Naur Form to describe the mini-language with the following description: Simple expressions limited to the variable identifiers x, y, or z, that contain the operations of addition (+), subtraction (-), and unary negation (~) together with parentheses.
```
Valid strings:
~x+~y
(x+z-y)
z-(x+y)
Invalid strings:
a+b
xy-xz
z(x+y)
```
```python
"""
BNF:
    <expression> ::= <term> | ~<term> | <expression><operator><term>
	<term>       ::= <expression> | (<expression>) | <sign>
	<sign>       ::= <identifier> | ~<identifier> 
	<operator>   ::= + | - 
    <identifier> ::= x | y | z
"""

import re


class Parser():
    def __init__(self, bnf: str, start_symbol: str):
        self._start_symbol = start_symbol
        self._bnf = self.list_terms(bnf)
        self._terms = dict()
        

    def list_terms(self, bnf) -> list:
        lines = bnf.strip().split('\n')
        for l in range(len(lines)):
            lines[l] = (lines[l].replace(' ', ''))
        
        return lines

    def prepare_production(self):
        for non_term in self._bnf:
            _ = non_term.split("::=")
            self._terms[_[0]] = _[1].split("|")
            

def main():
    bnf = "<expression> ::= <term> | <expression><operator><term>\n"
    bnf += ("<term>       ::= <expression> | (<expression>) | ~(<expression>) | <sign>\n")
    bnf += ("<sign>       ::= <identifier> | ~<identifier>\n")
    bnf += ("<operator>   ::= + | -\n")
    bnf += ("<identifier> ::= x | y | z\n")

    parse = Parser(bnf, "<expression>")
    parse.prepare_production()

if __name__ == "__main__":
    main()
```
### 2. Write a BNF grammar for the language of palindromes. Do not consider the spaces in evaluating the strings.
```
Palindrome: pop, pop a pop, a but tuba
Not a palindrome: hey, joe, the quick brown fox
```
```python

```
