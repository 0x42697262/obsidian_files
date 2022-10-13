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
        self._bnf = bnf
        self._terms = dict()
        self._terms["START_SYMBOL"] = start_symbol

    def list_terms(self, bnf) -> list:
        lines = bnf.strip().split('\n')
        for l in range(len(lines)):
            lines[l] = (lines[l].replace(' ', ''))
        
        return lines

    def prepare_production(self):
        for non_term in self._bnf:
            _ = non_term.split("::=")
            self._terms[_[0]] = _[1].split("|")

    def return_bnf(self) -> dict:
        return self._terms

    def start(self):
        self._bnf = self.list_terms(self._bnf)
        self.prepare_production()
            

class BNF_Interpreter():
    def __init__(self, bnf: list):
        self._bnf = bnf

    def verify(self, expression: str):
        is_valid = True
        str_expr = list(expression.replace(' ', ''))
        grammar = ""
        next_state = {
                    "~": ['~', '(', 'x', 'y', 'z'],
                    "(": ['~', '(', 'x', 'y', 'z'],
                    "x": ['+', '-', ')'],
                    "y": ['+', '-', ')'],
                    "z": ['+', '-', ')'],
                    "+": ['~', '(', 'x', 'y', 'z'],
                    "-": ['~', '(', 'x', 'y', 'z'],
                    ")": ['+', '-', ')']
                        }
        state = ['~', '(', 'x', 'y', 'z']
        
        buffer = [] 
        while is_valid and len(str_expr):
            if not len(buffer):
                 buffer.append("")
            c = str_expr.pop(0)
            if c in state:
                if c == '~':
                    buffer[-1] += '~'
                if c == "(":
                    if "<>" in grammar:
                        grammar = grammar.replace("<>", f"{buffer.pop()}<>", 1)
                        buffer.append("")
                        grammar = grammar.replace("<>", "(<>)<>", 1)
                    else:
                        grammar += buffer.pop()
                        grammar += "(<>)"
                if c == ")":
                    if "<>" in grammar:
                        grammar = grammar.replace("<>", buffer.pop(), 1)
                    else:
                        is_valid = False
                if c in self._bnf["<identifier>"]:
                    buffer[-1] += "<identifier>"
                if c in self._bnf["<operator>"]:
                    buffer[-1] += "<operator>"
                

                state = next_state[c]               

            else:
                 is_valid = False
        if len(buffer):
            grammar += buffer.pop()

        print(f"{expression} is valid: {is_valid} \n \"{grammar}\"")

def main():
    bnf = "<expression> ::= <term> | ~<term> | <expression><operator><term>\n"
    bnf += ("<term>       ::= <expression> | (<expression>) | <sign>\n")
    bnf += ("<sign>       ::= <identifier> | ~<identifier>\n")
    bnf += ("<operator>   ::= + | -\n")
    bnf += ("<identifier> ::= x | y | z\n")

    parse = Parser(bnf, "<expression>")
    parse.start()
    validate = BNF_Interpreter(parse.return_bnf())

    validate.verify("~x+~y")
    validate.verify("~~(x+z-y)")
    validate.verify("z-(x+y)")
    validate.verify("a+b")
    validate.verify("xy-xz")
    validate.verify("z(x+y)")
    ### EXTRAS
    validate.verify("z+(x+y))")
    validate.verify("~~((x+y)+~((x)+~y))")
    validate.verify("(~(x+~y))")
    validate.verify("~z+~x-~(~x+y-z)-(~((~x)))")
    validate.verify("((((((((y))))))))")
    validate.verify("(x+y+(x-z+(x-y-~(x-x+~(x+x+y))+z)+~x)+z+z+z+z+z)")

	validate.verify(input("Enter Test Case: "))

if __name__ == "__main__":
    main()

```
Source code for \#1 can be found [here](https://github.com/KrulYuno/obsidian_files/blob/master/Codes/basic_bnf_op.py):  https://github.com/KrulYuno/obsidian_files/blob/master/Codes/basic_bnf_op.py

### 2. Write a BNF grammar for the language of palindromes. Do not consider the spaces in evaluating the strings.
```
Palindrome: pop, pop a pop, a but tuba
Not a palindrome: hey, joe, the quick brown fox
```
```python

```
