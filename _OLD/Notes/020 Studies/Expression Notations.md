> [!INFO]
> Status: 
> Tags: #CMSC124

----
# Expression Notations
Types of Notations:
- [[Expression Notation - Infix|Infix]] 
- [[Expression Notation - Prefix|Prefix]] 
- [[Expression Notation - Postfix|Postfix]]

Basically, `A+(B*C)-((D-E)*(F+G))` is an infix expression. `+A*BC-*-DE+FG` should be the prefix expression equivalent. 

Converting the notations is easy, simply move the operator signs to the left or right based on the infix precedence.


References
---
- https://panda.ime.usp.br/panda/static/pythonds_pt/02-EDBasicos/InfixPrefixandPostfixExpressions.html
- https://stevenpcurtis.medium.com/infix-postfix-prefix-and-reverse-polish-notation-299affa57acf

My converter implementation of this in Rust: [[CMSC 124 Machine Problem 4]] (you can find the source code here)