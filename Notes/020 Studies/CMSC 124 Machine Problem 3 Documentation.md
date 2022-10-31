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
<int>     ::= <digit><int_>
<int_>    ::= <int> | ε
<digit>   ::= 0|1|2|3|4|5|6|7|8|9
```

Both grammars now satisfy:
1. Free from left recursion
2. It is now left factored

### Coding the arithmetic expression grammar
I started listing the token kinds or types for the first grammar. We need this for the lexer.
```rust
pub enum TokenKind {
    LITERALS(Vec<char>),
    OPEN_PAREN(char),
    CLOSE_PAREN(char),
    MUL_OP(char),
    DIV_OP(char),
    SUB_OP(char),
    ADD_OP(char),
    END_INPUT(char),
}
```
`LITERALS` should contain only the digits. There is no need to set it as integer for now. So, a vector of characters is enough.
`END_INPUT` is the last character input `$`.
The rest of the token kinds should be self explanatory.

Next is to create a struct for the lexer since rust does not have classes. See the reasons [here](https://doc.rust-lang.org/book/ch17-01-what-is-oo.html).
```rust
pub struct Lexer {
    input: Vec<char>,
    pub pos: usize,
    pub read_pos: usize,
    pub c: char,
}
```
`input` is the input strings but taken as a vector of characters.
`pos` reading position.
`read_pos` current moving reading position.
`c` current read character.
See [this](https://doc.rust-lang.org/book/ch03-02-data-types.html) for rust data types.

```rust
impl Lexer {
    pub fn new(input: Vec<char>) -> Self {...}
    pub fn read_char(&mut self) {...}
    pub fn next_token(&mut self) -> token::Token {...}
}
```
`pub fn new(input: Vec<char>) -> Self` initializes new instance of the lexer
`pub fn read_char(&mut self)` reads the next character `c` and increments the position `pos`
`pub fn next_token(&mut self)`  match the read character `c` then assign type to the token

This method returns itself with the inputs being initialized.
```rust
impl Lexer {
	pub fn new(input: Vec<char>) -> Self {
        Self {
            input,
            pos: 0,
            read_pos: 0,
            c: '0',
        }
    }
    
    ...
    
}
```
On the 4th line, `input,` does not need to be `input: input,` since rust can do shorthand struct initialization. See [this](https://doc.rust-lang.org/book/ch05-01-defining-structs.html#using-the-field-init-shorthand). Everything else inside the initialization starts at `0`.

```rust

```

I strictly follow the grammar rules so whitespaces are not ignored but instead considered as an invalid input.

### Coding the multi-digit decimal grammar

I was able to write the code for this machine problem thanks to [mohitk05's repository](https://github.com/mohitk05/monkey-rust) and a little reading of this [page](https://michael-f-bryan.github.io/static-analyser-in-rust/book/lex.html) about writing static analyzer for rust.

---
### Sources
- https://mohitkarekar.com/posts/pl/lexer/
- https://michael-f-bryan.github.io/static-analyser-in-rust/book/lex.html