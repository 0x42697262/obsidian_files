// #[derive(Debug, PartialEq)]
/*
 * GRAMMAR:
 *    <expr>   ::= +<num> | -<num> | <num>
 *    <num>    ::= <digit><num> | .<int> | <digit>
 *    <int>    ::= <digit><int> | <digit>
 *    <digit>  ::= 0|1|2|3|4|5|6|7|8|9
 */

pub enum TokenType {
    Digit(char),
    Dot(char),
    Sign(char),
    Illegal(char),
    End(char),
    None,
}

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
