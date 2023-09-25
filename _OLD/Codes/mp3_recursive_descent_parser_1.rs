// #[derive(Debug, PartialEq)]
/*
 * GRAMMAR:
 *  <expr>   ::= <term><expr_>
 *  <expr_>  ::= +<term><expr_> | -<term><expr_> | ε
 *  <term>   ::= <factor><term_>
 *  <term_>  ::= *<factor><term_> | /<factor><term_> | ε
 *  <factor> ::= (<expr>) |<digit>
 *  <digit>  ::= 0|1|2|3
 *
 */

pub enum TokenType {
    Integer(char),
    Operator(char),
    Parenthesis(char),
    Illegal(char),
    End(char),
    None,
}

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

pub struct Parser {
    input: String,
    pos: usize,
    token: TokenType,
}

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

fn main() {
    let mut p = Parser::new();
    loop {
        let mut expression = String::new();
        println!("Enter input string: ");
        let _input = std::io::stdin().read_line(&mut expression).unwrap();
        let expr = String::from(expression.trim());
        p.parse(expr);
        println!("");
    }
}
