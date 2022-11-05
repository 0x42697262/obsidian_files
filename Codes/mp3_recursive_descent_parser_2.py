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

/*
 * ====TOKENS====
 */
pub enum TokenKind {
    DIGITS(Vec<char>),
    DECIMAL(char),
    POSITIVE(char),
    NEGATIVE(char),
    END_INPUT(char),
    ILLEGAL(char),
}

/*
 * ====END TOKENS====
 */

fn is_digit(c: char) -> bool {
    '0' <= c && c <= '9'
}

/*
 * ====LEXICAL ANALYSER====
 */

pub struct Lexer {
    input: Vec<char>,
    pub pos: usize,
    pub read_pos: usize,
    pub c: char,
}

impl Lexer {
    pub fn new(input: Vec<char>) -> Self {
        Self {
            input,
            pos: 0,
            read_pos: 0,
            c: '$',
        }
    }

    pub fn read_char(&mut self) {
        if self.read_pos >= self.input.len() {
            self.c = '$';
        } else {
            self.c = self.input[self.read_pos];
        }
        self.pos = self.read_pos;
        self.read_pos = self.read_pos + 1;
    }

    pub fn next_token(&mut self) -> TokenKind {
        let read_num = |lex: &mut Lexer| -> Vec<char> {
            let pos = lex.pos;
            while lex.pos < lex.input.len() && is_digit(lex.c) {
                lex.read_char();
            }
            lex.input[pos..lex.pos].to_vec()
        };

        let token: TokenKind;
        match self.c {
            '+' => {
                token = TokenKind::POSITIVE('+');
            }
            '-' => {
                token = TokenKind::NEGATIVE('-');
            }
            '.' => {
                token = TokenKind::DECIMAL('.');
            }
            '$' => {
                token = TokenKind::END_INPUT('$');
            }
            _ => {
                if is_digit(self.c) {
                    let ident: Vec<char> = read_num(self);
                    return TokenKind::DIGITS(ident);
                } else {
                    token = TokenKind::ILLEGAL(self.c);
                }
            }
        }

        self.read_char();
        token
    }
}

/*
 * ====END LEXICAL ANALYSER====
 */

/*
 * ====PARSER====
 */
pub struct Parser {
    input: String,
    tokens: Vec<TokenKind>,
    token_pos: usize,
}

impl Parser {
    pub fn new() -> Self {
        Self {
            input: String::new(),
            tokens: Vec::new(),
            token_pos: 0,
        }
    }

    pub fn build_tokens(&mut self) {
        let mut lex = Lexer::new(self.input.chars().collect());
        lex.read_char();
        loop {
            let token: TokenKind = lex.next_token();
            if lex.pos <= self.input.len() {
                self.tokens.push(token);
            } else {
                break;
            }
        }
    }

    pub fn consume(&mut self) {
        if self.token_pos < self.tokens.len() {
            self.token_pos = self.token_pos + 1;
        }
    }

    pub fn parse(&mut self, input: String) -> bool {
        self.input = input;
        self.tokens = Vec::new();
        self.token_pos = 0;

        self.build_tokens();
        self.expr()
    }

    pub fn eof(&mut self) -> bool {
        true
    }
    pub fn illegal(&mut self) -> bool {
        false
    }

    pub fn expr(&mut self) -> bool {
        match self.tokens[self.token_pos] {
            TokenKind::POSITIVE('+') => {
                return self.operator();
            }
            TokenKind::NEGATIVE('-') => {
                return self.operator();
            }
            TokenKind::DIGITS(_) => {
                return self.digits();
            }
            _ => {
                return self.illegal();
            }
        }
    }

    pub fn operator(&mut self) -> bool {
        self.consume();
        match self.tokens[self.token_pos] {
            TokenKind::DIGITS(_) => {
                return self.digits();
            }
            _ => {
                return self.illegal();
            }
        }
    }

    pub fn digits(&mut self) -> bool {
        self.consume();
        match self.tokens[self.token_pos] {
            TokenKind::DECIMAL('.') => {
                return self.dot();
            }
            _ => {
                return self.illegal();
            }
        }
    }

    pub fn dot(&mut self) -> bool {
        self.consume();
        match self.tokens[self.token_pos] {
            TokenKind::DIGITS(_) => {
                return self.decimals();
            }
            _ => {
                return self.illegal();
            }
        }
    }

    pub fn decimals(&mut self) -> bool {
        self.consume();
        match self.tokens[self.token_pos] {
            TokenKind::END_INPUT('$') => {
                return self.eof();
            }
            _ => {
                return self.illegal();
            }
        }
    }
}
/*
 * ====END PARSER====
 */
fn main() {
    let mut par = Parser::new();

    println!("{}", par.parse(String::from("6$")));
    println!("{}", par.parse(String::from("-15.5$")));
    println!("{}", par.parse(String::from("+9.99$")));
    println!("{}", par.parse(String::from("33.369$")));
    println!("{}", par.parse(String::from("5.55.555$")));
    println!("{}", par.parse(String::from("a33$")));
    println!("{}", par.parse(String::from("++22.20$")));
    println!("{}", par.parse(String::from("+5.4.2$")));
    println!("{}", par.parse(String::from("$")));
    println!("{}", par.parse(String::from("$2")));
    println!("{}", par.parse(String::from("4-$")));
    println!("{}", par.parse(String::from("4-+$")));
}
