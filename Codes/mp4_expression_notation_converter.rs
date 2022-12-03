fn precedence_rank(token: Option<&char>) -> u32 {
    match token {
        Some(&'(') => return 1,
        Some(&')') => return 1,
        Some(&'+') => return 2,
        Some(&'-') => return 2,
        Some(&'*') => return 3,
        Some(&'/') => return 3,
        Some(&'^') => return 4,
        _ => return 0,
    }
}

fn result_to_string(result: Vec<char>) {
    let mut expression: String = "".to_owned();
    for c in result {
        expression.push(c);
    }
    println!("{}", expression);
}

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

fn postfix_to_infix(expression: &str) -> String {
    let mut stack: Vec<String> = Vec::new();

    for token in expression.chars() {
        match token {
            'A'..='Z' | 'a'..='z' => {
                stack.push(token.to_string());
            }
            '+' | '-' | '*' | '/' | '^' => {
                let operand_right: String = stack.pop().unwrap();
                let operand_left: String = stack.pop().unwrap();

                let mut temp_string: String = String::new();

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

fn postfix_to_prefix(expression: &str) -> String {
    let mut stack: Vec<String> = Vec::new();

    for token in expression.chars() {
        match token {
            'a'..='z' | 'A'..='Z' => {
                stack.push(token.to_string());
            }

            '+' | '-' | '*' | '/' | '^' => {
                let operand_right: String = stack.pop().unwrap();
                let operand_left: String = stack.pop().unwrap();

                let mut temp_string: String = String::new();
                temp_string.push(token);
                temp_string.push_str(&operand_left);
                temp_string.push_str(&operand_right);

                stack.push(temp_string);
            }
            _ => {}
        }
    }

    stack[0].to_owned()
}

fn prefix_to_infix(expression: &str) -> String {
    let mut stack: Vec<String> = Vec::new();

    for token in expression.chars().rev() {
        match token {
            'a'..='z' | 'A'..='Z' => {
                stack.push(token.to_string());
            }
            '+' | '-' | '*' | '/' | '^' => {
                let operand_left: String = stack.pop().unwrap();
                let operand_right: String = stack.pop().unwrap();
                let mut temp_string: String = String::new();

                temp_string.push('(');
                temp_string.push_str(&operand_left);
                temp_string.push(token);
                temp_string.push_str(&operand_right);
                temp_string.push(')');

                stack.push(temp_string);
            }
            _ => {}
        }
    }

    stack[0].to_owned()
}

fn prefix_to_postfix(expression: &str) -> String {
    let mut stack: Vec<String> = Vec::new();

    for token in expression.chars().rev() {
        match token {
            'a'..='z' | 'A'..='Z' => {
                stack.push(token.to_string());
            }
            '+' | '-' | '*' | '/' | '^' => {
                let operand_left: String = stack.pop().unwrap();
                let operand_right: String = stack.pop().unwrap();

                let mut temp_string: String = String::new();

                temp_string.push_str(&operand_left);
                temp_string.push_str(&operand_right);
                temp_string.push(token);

                stack.push(temp_string);
            }
            _ => {}
        }
    }

    stack[0].to_owned()
}

/*
 * --------------------------------------------------------------------
 */

fn check_notation_type(expression: &str) -> isize {
    match expression.chars().nth(0).unwrap() {
        '+' | '-' | '*' | '/' | '^' => {
            return -1;
        }
        _ => match expression.chars().nth_back(0).unwrap() {
            '+' | '-' | '*' | '/' | '^' => {
                return 1;
            }
            _ => return 0,
        },
    }
}

fn check_prefix(expression: &str) -> bool {
    let mut stack: Vec<String> = Vec::new();

    for token in expression.chars().rev() {
        match token {
            'a'..='z' | 'A'..='Z' => {
                stack.push(token.to_string());
            }
            '+' | '-' | '*' | '/' | '^' => {
                if stack.last() != None {
                    let operand_left: String = stack.pop().unwrap();
                    if stack.last() != None {
                        let operand_right: String = stack.pop().unwrap();
                        let mut temp_string: String = String::new();

                        temp_string.push_str(&operand_left);
                        temp_string.push_str(&operand_right);
                        temp_string.push(token);

                        stack.push(temp_string);
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            }
            ' ' => {}
            _ => return false,
        }
    }

    if stack.len() != 1 {
        return false;
    }
    true
}

fn check_postfix(expression: &str) -> bool {
    let mut stack: Vec<String> = Vec::new();

    for token in expression.chars() {
        match token {
            'a'..='z' | 'A'..='Z' => {
                stack.push(token.to_string());
            }
            '+' | '-' | '*' | '/' | '^' => {
                if stack.last() != None {
                    let operand_right: String = stack.pop().unwrap();
                    if stack.last() != None {
                        let operand_left: String = stack.pop().unwrap();
                        let mut temp_string: String = String::new();

                        temp_string.push_str(&operand_left);
                        temp_string.push_str(&operand_right);
                        temp_string.push(token);

                        stack.push(temp_string);
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            }
            ' ' => {}
            _ => return false,
        }
    }
    if stack.len() != 1 {
        return false;
    }
    true
}

fn main() {
    let mut expression: String = String::new();
    std::io::stdin()
        .read_line(&mut expression)
        .expect("Incorrect expression input.");

    let expression_type: isize = check_notation_type(&expression);
}

/*
 * UNIT TESTING
 * Run `cargo test` to begin testing
 *     *assuming that a cargo project is initiated
 */

#[cfg(test)]
mod check_notations_test {
    use super::*;

    #[test]
    fn check_postfix_test() {
        assert_eq!(check_postfix("ab+c*d-"), true);
        assert_eq!(check_postfix("ab+"), true);
        assert_eq!(check_postfix("A"), true);
        assert_eq!(check_postfix("ABCD+*-"), true);
        assert_eq!(check_postfix("AB+C+D+"), true);
        assert_eq!(check_postfix("AB+AB*+"), true);
        assert_eq!(check_postfix("A B + A  B * +"), true);

        assert_eq!(check_postfix("AB+AB+"), false);
        assert_eq!(check_postfix("AB++AB+"), false);
        assert_eq!(check_postfix("A B + + A B+"), false);
        assert_eq!(check_postfix("(AB++AB+)"), false);
        assert_eq!(check_postfix("ABAB++"), false);
        assert_eq!(check_postfix("ABAB+++++"), false);
        assert_eq!(check_postfix("++"), false);
        assert_eq!(check_postfix("+AB"), false);
        assert_eq!(check_postfix("+AB-"), false);
        assert_eq!(check_postfix("AB++"), false);
        assert_eq!(check_postfix("AB"), false);
        assert_eq!(check_postfix("A+B"), false);
        assert_eq!(check_postfix("++A"), false);
        assert_eq!(check_postfix("AaaA"), false);
    }

    #[test]
    fn check_prefix_test() {
        assert_eq!(check_prefix("+AB"), true);
        assert_eq!(check_prefix("*+AB-SW"), true);
        assert_eq!(check_prefix("+ A B"), true);
        assert_eq!(check_prefix("/*+AB+CD+GF"), true);
        assert_eq!(check_prefix("+ A   B"), true);

        assert_eq!(check_prefix("+AB+"), false);
        assert_eq!(check_prefix("+-AB"), false);
        assert_eq!(check_prefix("AB"), false);
        assert_eq!(check_prefix("+++"), false);
        assert_eq!(check_prefix("(+AB)"), false);
        assert_eq!(check_prefix("+  () AB"), false);
        assert_eq!(check_prefix("A+AB"), false);
        assert_eq!(check_prefix("A+A+B"), false);
        assert_eq!(check_prefix("AB+"), false);
    }
}

#[cfg(test)]
mod notation_conversion_tests {
    use super::*;

    #[test]
    fn infix_to_postfix_test() {
        assert_eq!(
            infix_to_postfix("A+B*C+D"),
            ['A', 'B', 'C', '*', '+', 'D', '+']
        );
        assert_eq!(
            infix_to_postfix("(A+B)*(C+D)"),
            ['A', 'B', '+', 'C', 'D', '+', '*']
        );
        assert_eq!(
            infix_to_postfix("A*B+C*D"),
            ['A', 'B', '*', 'C', 'D', '*', '+']
        );
        assert_eq!(
            infix_to_postfix("A+B+C+D"),
            ['A', 'B', '+', 'C', '+', 'D', '+']
        );
        assert_eq!(infix_to_postfix("(A+B)*C"), ['A', 'B', '+', 'C', '*']);
        assert_eq!(
            infix_to_postfix("A*B+C/D"),
            ['A', 'B', '*', 'C', 'D', '/', '+']
        );
        assert_eq!(
            infix_to_postfix("A*(B+C)/D"),
            ['A', 'B', 'C', '+', '*', 'D', '/']
        );
        assert_eq!(
            infix_to_postfix("a*(b+c/d)"),
            ['a', 'b', 'c', 'd', '/', '+', '*']
        );
        assert_eq!(infix_to_postfix("a*(b+c)"), ['a', 'b', 'c', '+', '*']);
        assert_eq!(
            infix_to_postfix("a/b+c/d"),
            ['a', 'b', '/', 'c', 'd', '/', '+']
        );
        assert_eq!(
            infix_to_postfix("((a+b)*c)-d"),
            ['a', 'b', '+', 'c', '*', 'd', '-']
        );
        assert_eq!(
            infix_to_postfix("(a+(((b*c)-((d/(e^f))*g))*h))"),
            ['a', 'b', 'c', '*', 'd', 'e', 'f', '^', '/', 'g', '*', '-', 'h', '*', '+']
        );
    }

    #[test]
    fn infix_to_prefix_test() {
        assert_eq!(
            infix_to_prefix("A+B*C+D"),
            ['+', '+', 'A', '*', 'B', 'C', 'D']
        );
        assert_eq!(
            infix_to_prefix("(A+B)*(C+D)"),
            ['*', '+', 'A', 'B', '+', 'C', 'D']
        );
        assert_eq!(
            infix_to_prefix("A*B+C*D"),
            ['+', '*', 'A', 'B', '*', 'C', 'D']
        );
        assert_eq!(
            infix_to_prefix("A+B+C+D"),
            ['+', '+', '+', 'A', 'B', 'C', 'D']
        );
        assert_eq!(infix_to_prefix("(A+B)*C"), ['*', '+', 'A', 'B', 'C']);
        assert_eq!(
            infix_to_prefix("A*B+C/D"),
            ['+', '*', 'A', 'B', '/', 'C', 'D']
        );
        assert_eq!(
            infix_to_prefix("A*(B+C)/D"),
            ['/', '*', 'A', '+', 'B', 'C', 'D']
        );
        assert_eq!(
            infix_to_prefix("a*(b+c/d)"),
            ['*', 'a', '+', 'b', '/', 'c', 'd']
        );
        assert_eq!(infix_to_prefix("a*(b+c)"), ['*', 'a', '+', 'b', 'c']);
        assert_eq!(
            infix_to_prefix("a/b+c/d"),
            ['+', '/', 'a', 'b', '/', 'c', 'd']
        );
        assert_eq!(
            infix_to_prefix("((a+b)*c)-d"),
            ['-', '*', '+', 'a', 'b', 'c', 'd']
        );
        assert_eq!(
            infix_to_prefix("(a+(((b*c)-((d/(e^f))*g))*h))"),
            ['+', 'a', '*', '-', '*', 'b', 'c', '*', '/', 'd', '^', 'e', 'f', 'g', 'h']
        );
    }
    #[test]
    fn postfix_to_infix_test() {
        assert_eq!(postfix_to_infix("ABC*+D+"), "((A+(B*C))+D)");
        assert_eq!(postfix_to_infix("AB+CD+*"), "((A+B)*(C+D))");
        assert_eq!(postfix_to_infix("AB*CD*+"), "((A*B)+(C*D))");
        assert_eq!(postfix_to_infix("AB+C+D+"), "(((A+B)+C)+D)");
        assert_eq!(postfix_to_infix("AB+C*"), "((A+B)*C)");
        assert_eq!(postfix_to_infix("AB*CD/+"), "((A*B)+(C/D))");
        assert_eq!(postfix_to_infix("ABC+*D/"), "((A*(B+C))/D)");
        assert_eq!(postfix_to_infix("abcd/+*"), "(a*(b+(c/d)))");
        assert_eq!(postfix_to_infix("abc+*"), "(a*(b+c))");
        assert_eq!(postfix_to_infix("ab/cd/+"), "((a/b)+(c/d))");
        assert_eq!(postfix_to_infix("ab+c*d-"), "(((a+b)*c)-d)");
        assert_eq!(
            postfix_to_infix("abc*def^/g*-h*+"),
            "(a+(((b*c)-((d/(e^f))*g))*h))"
        );
    }
    #[test]
    fn postfix_to_prefix_test() {
        assert_eq!(postfix_to_prefix("ABC*+D+"), "++A*BCD");
        assert_eq!(postfix_to_prefix("AB+CD+*"), "*+AB+CD");
        assert_eq!(postfix_to_prefix("AB*CD*+"), "+*AB*CD");
        assert_eq!(postfix_to_prefix("AB+C+D+"), "+++ABCD");
        assert_eq!(postfix_to_prefix("AB+C*"), "*+ABC");
        assert_eq!(postfix_to_prefix("AB*CD/+"), "+*AB/CD");
        assert_eq!(postfix_to_prefix("ABC+*D/"), "/*A+BCD");
        assert_eq!(postfix_to_prefix("abcd/+*"), "*a+b/cd");
        assert_eq!(postfix_to_prefix("abc+*"), "*a+bc");
        assert_eq!(postfix_to_prefix("ab/cd/+"), "+/ab/cd");
        assert_eq!(postfix_to_prefix("ab+c*d-"), "-*+abcd");
        assert_eq!(postfix_to_prefix("abc*def^/g*-h*+"), "+a*-*bc*/d^efgh");
    }
    #[test]
    fn prefix_to_infix_test() {
        assert_eq!(prefix_to_infix("++A*BCD"), "((A+(B*C))+D)");
        assert_eq!(prefix_to_infix("*+AB+CD"), "((A+B)*(C+D))");
        assert_eq!(prefix_to_infix("+*AB*CD"), "((A*B)+(C*D))");
        assert_eq!(prefix_to_infix("+++ABCD"), "(((A+B)+C)+D)");
        assert_eq!(prefix_to_infix("*+ABC"), "((A+B)*C)");
        assert_eq!(prefix_to_infix("+*AB/CD"), "((A*B)+(C/D))");
        assert_eq!(prefix_to_infix("/*A+BCD"), "((A*(B+C))/D)");
        assert_eq!(prefix_to_infix("*a+b/cd"), "(a*(b+(c/d)))");
        assert_eq!(prefix_to_infix("*a+bc"), "(a*(b+c))");
        assert_eq!(prefix_to_infix("+/ab/cd"), "((a/b)+(c/d))");
        assert_eq!(prefix_to_infix("-*+abcd"), "(((a+b)*c)-d)");
        assert_eq!(
            prefix_to_infix("+a*-*bc*/d^efgh"),
            "(a+(((b*c)-((d/(e^f))*g))*h))"
        );
    }

    #[test]
    fn prefix_to_postfix_test() {
        assert_eq!(prefix_to_postfix("++A*BCD"), "ABC*+D+");
        assert_eq!(prefix_to_postfix("*+AB+CD"), "AB+CD+*");
        assert_eq!(prefix_to_postfix("+*AB*CD"), "AB*CD*+");
        assert_eq!(prefix_to_postfix("+++ABCD"), "AB+C+D+");
        assert_eq!(prefix_to_postfix("*+ABC"), "AB+C*");
        assert_eq!(prefix_to_postfix("+*AB/CD"), "AB*CD/+");
        assert_eq!(prefix_to_postfix("/*A+BCD"), "ABC+*D/");
        assert_eq!(prefix_to_postfix("*a+b/cd"), "abcd/+*");
        assert_eq!(prefix_to_postfix("*a+bc"), "abc+*");
        assert_eq!(prefix_to_postfix("+/ab/cd"), "ab/cd/+");
        assert_eq!(prefix_to_postfix("-*+abcd"), "ab+c*d-");
        assert_eq!(prefix_to_postfix("+a*-*bc*/d^efgh"), "abc*def^/g*-h*+");
    }
}
