CMSC 124 Problem Set 2  
**Topic Coverage**: Syntax and Semantics

### 1. Write a syntactic specification using Backus-Naur Form to describe the mini-language with the following description: Simple expressions limited to thevariable identifiers x, y, or z, that contain the operations of addition (+),subtraction (-), and unary negation (~) together with parentheses.
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

### 2. Write a BNF grammar for the language of palindromes. Do not consider the spaces in evaluating the strings.
```
Palindrome: pop, pop a pop, a but tuba
Not a palindrome: hey, joe, the quick brown fox
```
