
CMSC 124 Machine Problem 4
**Topic Coverage**: Expressions

---

Install [rust](https://doc.rust-lang.org/book/ch01-01-installation.html) or use [Rust Playground](https://play.rust-lang.org/) on your web browser.

---

## 1. Create a program that will accept an expression in infix notation and is capable of converting it to prefix as well as postfix notation. Similarly, you should also be able to accept an expression in prefix notation and convert it to infix and postfix notation; and accept an expression in postfix notation, and convert it to infix and prefix notation. Assumelikewise that an expression can be erroneous, thus provide appropriate error-handling schemes.

| **Input** | **postfix**                    | 
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

Source Code: 

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

Source Code:

---

## Solution to problem 1:
Stack will be used to implement the conversion process.

**Converting Infix expression to Postfix expression**:
1. Create a stack `op_stack` for operators and an postfix list `postfix`.
2. .Create a precedence rank for the operators:
	1. `^` (highest)
	2. `*` and `/`
	3. `+` and `-`
	4. `(` (lowest)
3. Loop each tokens of the infix expression. Notice that each tokens only contains one character.
	1. If the character token is an *operand*, append to `postfix` (e.g. A or B)
	2. If the character token is a left parenthesis, push to `op_stack`.
	3. If the character token is a right parenthesis, pop every items in the `op_stack` until the corresponding left parenthesis is popped. Append each operator to `postfix`.
	4. If the character token is an *operator* (e.g. + or \*), remove existing then append to `postfix` the higher or equal precedence operators in the `op_stack` and then push the operator to the `op_stack`.
4. Once all tokens are processed, pop all tokens in `op_stack` and append it to `postfix`. 
```rust
fn infix_to_postfix(expression: &str) -> Vec<char> {
    let mut op_stack: Vec<char> = Vec::new();
    let mut postfix: Vec<char> = Vec::new();
    for token in expression.chars() {
        match token {
            'a'..='z' | 'A'..='Z' => {
                postfix.push(token);
            }
            '(' => {
                op_stack.push(token);
            }
            ')' => {
                let mut top_token: Option<char> = op_stack.pop();
                while top_token != Some('(') {
                    postfix.push(top_token.unwrap());
                    top_token = op_stack.pop();
                }
            }
             '+' | '-' | '*' | '/' | '^' => {
                while !op_stack.is_empty()
                    && precedence_rank(op_stack.last()) >= precedence_rank(Some(&token))
                {
                    postfix.push(op_stack.pop().unwrap());
                }
                op_stack.push(token);
            }
            _ => {}
        }
    }
    while !op_stack.is_empty() {
        postfix.push(op_stack.pop().unwrap());
    }
    postfix
}
```
`infix_to_postfix()` function takes input as string and iterates each characters as a token from left to right. This function returns a vector of characters.

**Converting Infix expression to Prefix expression**:
Stack is used to convert the expression.

The same method is implemented in converting infix to prefix from infix to postfix, except iteration is reversed.
```rust
fn infix_to_prefix(expression: &str) -> Vec<char> {
    let mut op_stack: Vec<char> = Vec::new();
    let mut prefix: Vec<char> = Vec::new();
    for token in expression.chars().rev() {
        match token {
            'a'..='z' | 'A'..='Z' => {
                prefix.push(token);
            }
            ')' => {
                op_stack.push(token);
            }
            '(' => {
                let mut top_token: Option<char> = op_stack.pop();
                while top_token != Some(')') {
                    prefix.push(top_token.unwrap());
                    top_token = op_stack.pop();
                }
            }
            '+' | '-' | '*' | '/' | '^' => {
                while !op_stack.is_empty()
                    && precedence_rank(op_stack.last()) > precedence_rank(Some(&token))
                {
                    prefix.push(op_stack.pop().unwrap());
                }
                op_stack.push(token);
            }
            _ => {}
        }
    }
    while !op_stack.is_empty() {
        prefix.push(op_stack.pop().unwrap());
    }
    prefix.reverse();
    prefix
}
```
Notice that the iteration starts from the end of the index `for token in expression.chars().rev()` and the checks for the parenthesis have switched.

**Converting Postfix expression to Infix expression***
Stacks is implemented for the conversion.

1. Create stack `stack` for storing the operands.
2. Iterate through the expression, token by token.
3. If token is an operand, push it to `stack`
4. If token is an operator, pop the `stack` two times
	1. First pop, set it as the right operand `operand_right`
	2. Second pop, set it as the left operand `operand_left`
5. Push: ( `operand_left` token `operand_right` )
```rust
fn postfix_to_infix(expression: &str) -> String {
    let mut stack: Vec<String> = Vec::new();
    for token in expression.chars() {
        match token {
            'A'..='Z' | 'a'..='z' => {
                stack.push(token.to_string());
            }
            '+' | '-' | '*' | '/' | '^' => {
                let operand_right: String;
                let operand_left: String;
                let mut temp_string: String = String::new();
                operand_right = stack.pop().unwrap();
                operand_left = stack.pop().unwrap();
                temp_string.push('(');
                temp_string.push_str(&operand_left);
                temp_string.push(token);
                temp_string.push_str(&operand_right);
                temp_string.push(')');
                stack.push(temp_string.to_owned());
            }
            _ => {}
        }
    }
    stack[0].to_owned()
}
```
Unlike other functions, this returns a String instead of a character vector.




## Solution to number 2:


# References
---
_2.9. Infix, Prefix and Postfix Expressions — Resolução de Problemas Usando Python_. (n.d.). https://panda.ime.usp.br/panda/static/pythonds_pt/02-EDBasicos/InfixPrefixandPostfixExpressions.html