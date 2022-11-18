
CMSC 124 Machine Problem 4
**Topic Coverage**: Expressions

---

Install [rust](https://doc.rust-lang.org/book/ch01-01-installation.html) or use [Rust Playground](https://play.rust-lang.org/) on your web browser.

---

## 1. Create a program that will accept an expression in infix notation and is capable of converting it to prefix as well as postfix notation. Similarly, you should also be able to accept an expression in prefix notation and convert it to infix and postfix notation; and accept an expression in postfix notation, and convert it to infix and prefix notation. Assumelikewise that an expression can be erroneous, thus provide appropriate error-handling schemes.

| **Input** | **Output**                    | 
| --------- | ----------------------------- |
| Infix     | Prefix and postfix equivalent |
| Prefix    | Infix and postfix equivalent  |
| Postfix   | Infix and prefix equivalent   |
^Ypn5Cf

Sample expressions:
| Infix                            | Prefix           | Postfix            |
| -------------------------------- | ---------------- | ------------------ |
| A+B\*C+D                         | ++A\*BCD         | ABC\*+D+           |
| (A+B)\*(C+D)                     | \*+AB+CD         | AB+CD+\*           |
| A\*B+C\*D                        | +\*AB\*CD        | AB\*CD\*+          |
| A+B+C+D                          | +++ABCD          | AB+C+D+            |
| (A+B)\*C                         | \*+ABC           | AB+C\*             |
| A\*B+C/D                         | +\*AB/CD         | AB\*CD/+           |
| A\*(B+C)/D                       | /\*A+BCD         | ABC+\*D/           |
| a\*(b+c/d)                       | \*a+b/cd         | abcd/+\*           |
| a\*(b+c)                         | \*a+bc           | abc+\*             |
| a/b+c/d                          | +/ab/cd          | ab/cd/+            |
| ((a+b)\*c)-d                     | -\*+abcd         | ab+c\*d-           |
| (a+(((b\*c)-((d/(e^f))\*g))\*h)) | +a\*-*bc*/d^efgh | abc\*def^/g\*-h\*+ |
^5aqOWm

## 2. Use the same algorithms you have implemented in #1 to accept an expression (this time variables are actual numbers) and evaluate them to give the final answer. For clarity purposes, separate each token with a space. Also, assume that user may input erroneous expressions, so include exception handling in your implementation. Shown below are some example runs:
Expression: 6 2 3 + - 3 8 2 / + * 2 ^ 3 +
Answer: 52

Expression: + 9 * 2 6
Answer: 21

Expression: - + 7 * 4 5 + 2 0
Answer: 25

Expression: - + 8 / 6 3 2
Answer: 8

Expression: ( 5 + 10 ) / ( 20 / 4 )
Answer: 3

---

## Solution to problem 1:

**Converting Infix expression to Postfix expression**:
1. Create a stack `op_stack` for operators and an output list `output`.
2. Create a precedence rank for the operators:
	1. `^` 4 (highest)
	2. `*` and `/` 3
	3. `+` and `-` 2
	4. `(` 1 (lowest)
3. Loop each tokens of the infix expression. Notice that each tokens only contains one character.
	1. If the character token is an *operand*, append to `output` (e.g. A or B)
	2. If the character token is a left parenthesis, push to `op_stack`.
	3. If the character token is a right parenthesis, pop every items in the `op_stack` until the corresponding left parenthesis is popped. Append each operator to `output`.
	4. If the character token is an *operator* (e.g. + or \*), remove existing then append to `output` the higher or equal precedence operators in the `op_stack` and then push the operator to the `op_stack`.
4. Once all tokens are processed, pop all tokens in `op_stack` and append it to `output`. 




# References
---
_2.9. Infix, Prefix and Postfix Expressions — Resolução de Problemas Usando Python_. (n.d.). https://panda.ime.usp.br/panda/static/pythonds_pt/02-EDBasicos/InfixPrefixandPostfixExpressions.html