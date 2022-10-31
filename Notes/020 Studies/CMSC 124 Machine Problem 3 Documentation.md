> [!INFO]
> Status: #WIP
> Tags: #CMSC124 #Machine_Problem 

----
# CMSC 124 Machine Problem 3 Documentation

To run the codes, install [rust](https://doc.rust-lang.org/book/ch01-01-installation.html) on your PC or use [Rust Playground](https://play.rust-lang.org/) on your web browser. See [[CMSC 124 Machine Problem 3]].

---
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
<int>     ::= <digit> | <digit><digit>
<digit>   ::= 0|1|2|3|4|5|6|7|8|9
```
### Coding

