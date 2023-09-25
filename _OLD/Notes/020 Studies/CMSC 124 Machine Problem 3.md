CMSC 124 Machine Problem 3 
**Topic Coverage**: Lexical and Syntax Analysis

---

Install [rust](https://doc.rust-lang.org/book/ch01-01-installation.html) or use [Rust Playground](https://play.rust-lang.org/) on your web browser.

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

Solution: https://replit.com/@KrulYuno/CMSC124-Machine-Problem-31#main.rs or https://github.com/KrulYuno/obsidian_files/blob/master/Codes/mp3_recursive_descent_parser_1.rs

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

Solution: https://github.com/KrulYuno/obsidian_files/blob/master/Codes/mp3_recursive_descent_parser_2.rs or https://replit.com/@KrulYuno/CMSC124-Machine-Problem-32#src/main.rs

---

## Rewriting The Grammars
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
<expr>   ::= +<num> | -<num> | <num>  
<num>    ::= <digit><num> | .<int> | <digit>
<int>    ::= <digit><int> | <digit>
<digit>  ::= 0|1|2|3|4|5|6|7|8|9
```

Both grammars now satisfy:
1. Free from left recursion
2. It is now left factored

## Implementing The Grammars
### Coding the arithmetic expression grammar
Create token types for the lexemes. Each token types takes one character input except `None` since it is not part of the grammar tokens.
```rust
pub enum TokenType {
    Integer(char),
    Operator(char),
    Parenthesis(char),
    Illegal(char),
    End(char),
    None,
}
```

Create a method for tokenzing the lexemes based on the token type enum `TokenType`.
```rust
fn lex(lexeme: char) -> TokenType {
    match lexeme {
        '+' | '-' | '*' | '/' => return TokenType::Operator(lexeme),
        '0'..='3' => return TokenType::Integer(lexeme),
        '(' => return TokenType::Parenthesis('('),
        ')' => return TokenType::Parenthesis(')'),
        '$' => return TokenType::End('$'),
        _ => return TokenType::Illegal(lexeme),
    }
}
```
Takes a character and matches the lexeme to its token type. 
Rust's [Pattern Matching](https://doc.rust-lang.org/rust-by-example/flow_control/match.html) is similar to C++ switch statements.

Define a parser [struct](https://doc.rust-lang.org/book/ch05-01-defining-structs.html.
```rust
pub struct Parser {
    input: String,
    pos: usize,
    token: TokenType,
}
```
`input` string expression input.
`pos` index of the token type of the lexeme.
`token` token type of the lexeme.

Implement parser struct by instantiating it through `new()` method.
`parse()` takes string expression as input argument and proceeds to execute recursive-descent parsing.
`next()` increments `pos` index.
```rust
impl Parser {
    pub fn new() -> Self {
        Self {
            input: String::new(),
            pos: 0,
            token: TokenType::None,
        }
    }

    pub fn parse(&mut self, input: String) -> bool {
        self.input = input;
        self.pos = 0;
        self.token = lex(self.input.chars().nth(self.pos).unwrap());

        self.next();
        self.expr();

        if matches!(self.token, TokenType::End('$')) && self.pos - 1 == self.input.len() - 1 {
            println!("VALID EXPRESSION: {}", self.input);
            return true;
        } else {
            panic!("Expected '$'");
        }
    }

    pub fn next(&mut self) {
        if self.pos < self.input.len() {
            self.token = lex(self.input.chars().nth(self.pos).unwrap());
            self.pos = self.pos + 1;
        }
    }

    pub fn expr(&mut self) {
        self.term();
        self.expr_();
    }

    pub fn expr_(&mut self) {
        if matches!(self.token, TokenType::Operator('+'))
            || matches!(self.token, TokenType::Operator('-'))
        {
            self.next();
            self.term();
            self.expr_();
        }
    }

    pub fn term(&mut self) {
        self.factor();
        self.term_();
    }

    pub fn term_(&mut self) {
        if matches!(self.token, TokenType::Operator('*'))
            || matches!(self.token, TokenType::Operator('/'))
        {
            self.next();
            self.factor();
            self.term_();
        }
    }

    pub fn factor(&mut self) {
        if matches!(self.token, TokenType::Integer(_)) {
            self.next();
        } else if matches!(self.token, TokenType::Parenthesis('(')) {
            self.next();
            self.expr();

            if matches!(self.token, TokenType::Parenthesis(')')) {
                self.next();
            } else {
                self.illegal(String::from("Expected (<expr>)"));
            }
        } else {
            self.illegal(String::from("Expected (<expr>) or <digit>"));
        }
    }

    pub fn illegal(&mut self, error: String) {
        panic!("Invalid expression: {}", error);
    }
}
```
This implementation does not ignore whitespaces so they get treated as an illegal character.

### Coding the multi-digit decimal grammar
Implementing the recursive-descent parser is similar to the previous grammar's implemention with minor changes.

This parser uses different token types but some remains the same.
```rust
pub enum TokenType {
    Digit(char),
    Dot(char),
    Sign(char),
    Illegal(char),
    End(char),
    None,
}
```

The lexer has similar structure but modified to follow the tokenization.
```rust
fn lex(lexeme: char) -> TokenType {
    match lexeme {
        '0'..='9' => {
            return TokenType::Digit(lexeme);
        }
        '+' | '-' => {
            return TokenType::Sign(lexeme);
        }
        '.' => {
            return TokenType::Dot('.');
        }
        '$' => {
            return TokenType::End('$');
        }
        _ => {
            return TokenType::Illegal(lexeme);
        }
    }
}
```

Same struct for the parser initializers
```rust
pub struct Parser {
    input: String,
    pos: usize,
    token: TokenType,
}
```

Then implement the struct parser.
```rust
impl Parser {
    pub fn new() -> Self {
        Self {
            input: String::new(),
            pos: 0,
            token: TokenType::None,
        }
    }

    pub fn parse(&mut self, input: String) -> bool {
        self.input = input;
        self.pos = 0;
        self.token = lex(self.input.chars().nth(self.pos).unwrap());

        self.next();
        self.expr();

        if matches!(self.token, TokenType::End('$')) && self.pos - 1 == self.input.len() - 1 {
            println!("VALID EXPRESSION: {}", self.input);
            return true;
        } else {
            println!("INVALID EXPRESSION: {}", self.input);
            return false;
        }
    }

    pub fn next(&mut self) {
        if self.pos < self.input.len() {
            self.token = lex(self.input.chars().nth(self.pos).unwrap());
            self.pos = self.pos + 1;
        } else {
            self.token = TokenType::None;
        }
    }

    pub fn expr(&mut self) {
        if matches!(self.token, TokenType::Digit(_)) || matches!(self.token, TokenType::Dot('.')) {
            self.num();
        } else if matches!(self.token, TokenType::Sign(_)) {
            self.next();
            self.num();
        } else {
            self.illegal(String::from("Expected +<num>, -<num>, or <num>"));
        }
    }

    pub fn num(&mut self) {
        if matches!(self.token, TokenType::Digit(_)) {
            self.next();
            self.num();
        } else if matches!(self.token, TokenType::Dot('.')) {
            self.next();
            if matches!(self.token, TokenType::End('$')) {
                panic!("Expected <digit>, not $");
            }
            self.int();
        } else if matches!(self.token, TokenType::End('$')) {
        } else {
            panic!("Expected <digit>");
        }
    }

    pub fn int(&mut self) {
        if matches!(self.token, TokenType::Digit(_)) {
            self.next();
            self.int();
        } else if matches!(self.token, TokenType::End('$')) {
        } else {
            panic!("Expected <digit>");
        }
    }

    pub fn illegal(&mut self, error: String) {
        panic!("Invalid Expression: {}", error);
    }
}
```

---
### References
- _Papers with Code - Eliminating Left Recursion without the Epsilon_. (2019, August 28). https://cs.paperswithcode.com/paper/eliminating-left-recursion-without-the
- Karekar, M. (n.d.). _Starting with a Lexer - in Rust_. mohitkarekar.com. Retrieved October 31, 2022, from https://mohitkarekar.com/posts/pl/lexer/
- _Lexing - Create a Static Analyser in Rust_. (n.d.). Retrieved October 31, 2022, from https://michael-f-bryan.github.io/static-analyser-in-rust/book/lex.html