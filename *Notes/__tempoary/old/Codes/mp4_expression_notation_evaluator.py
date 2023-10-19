def precedence_rank(token: str):
    match token:
        case '(':
            return 1
        case ')':
            return 1
        case '+':
            return 2
        case '-':
            return 2
        case '*':
            return 3
        case '/':
            return 3
        case '^':
            return 4
        case _:
            return 0


def number_identifier(number:str):
    try:
        return int(number)
    except:
        return None


def arithmetic_operations(operator, left, right):
    match operator:
        case '+':
            return left + right
        case '-':
            return left - right
        case '*':
            return left * right
        case '/':
            return left / right
        case '^':
            return left ** right
        case _:
            return None


def evaluate_postfix(expression: str):
    tokens      = expression.split()
    stack       = list()
    
    for token in tokens:
        if number_identifier(token) == None:
            match token:
                case '+' | '-' | '*' | '/' | '^':
                    try:
                        operand_right   = stack.pop()
                        operand_left    = stack.pop()
                        value           = arithmetic_operations(token, operand_left, operand_right)
                        stack.append(value)
                    except:
                        print("Invalid Expression.")
                        return None
                    
                case _:
                    print("Invalid Expression.")
                    return None

        else:
            stack.append(number_identifier(token))
    
    if len(stack) != 1:
        print("Invalid Expression.")
        return None

    return stack[0]

def evaluate_prefix(expression: str):
    tokens      = expression.split()
    stack       = list()

    tokens.reverse()
    for token in tokens:
        if number_identifier(token) == None:
            match token:
                case '+' | '-' | '*' | '/' | '^':
                    try:
                        operand_left    = stack.pop()
                        operand_right   = stack.pop()
                        value           = arithmetic_operations(token, operand_left, operand_right)
                        stack.append(value)
                    except:
                        print("Invalid Expression.")
                        return None

                case _:
                    print("Invalid Expression.")
                    return None

        else:
            stack.append(number_identifier(token))

    if len(stack) != 1:
        print("Invalid Expression.")
        return None

    return stack[0]


def infix_to_postfix(expression: str):
    tokens          = expression.split()
    operator_stack  = list()
    postfix_stack   = list()

    for token in tokens:
        number_token    = number_identifier(token)
        if number_token == None:
            match token:
                case '+' | '-' | '*' | '/' | '^':
                    while len(operator_stack) > 0 \
                        and precedence_rank(operator_stack[-1]) >= precedence_rank(token):
                        try:
                            postfix_stack.append(operator_stack.pop())        
                        except:
                            print("Invalid Expression.")
                            return None
                    operator_stack.append(token)

                case '(':
                       operator_stack.append(token)

                case ')':
                    try:
                        top_token   = operator_stack.pop()
                        while top_token != '(': 
                            postfix_stack.append(top_token)
                            top_token   = operator_stack.pop()

                    except:
                        print("Invalid Expression.")
                        return None

                case _:
                    print("Invalid Expression.")
                    return None
        else:
            postfix_stack.append(number_token)

    while len(operator_stack) > 0:
        try:
            postfix_stack.append(operator_stack.pop())
        except:
            print("Invalid Expression.")
            return None

    return ' '.join(map(str, postfix_stack))


# ------------------------------------------------------------------------------------------------- #

def check_notation_type(expression: str) -> int:
    if expression[0] in ['-', '+', '*', '/', '^']:
        return -1
    elif expression[-1] in ['-', '+', '*', '/', '^']: 
        return 1
    else:
        return 0


# ------------------------------------------------------------------------------------------------- #


def main():
    print(infix_to_postfix("1 - 2  3"))

    input_expression    = input("Enter Expression: ")
    match check_notation_type(input_expression):
        case -1:
            answer  = evaluate_prefix(input_expression)
            if answer != None:
                print(answer)
        case 0:
            try:
                answer = evaluate_postfix(infix_to_postfix(input_expression))
                if answer != None:
                    print(answer)
            except:
                print("Invalid Expression.")
                return None
        case 1:
            answer  = evaluate_postfix(input_expression)
            if answer != None:
                print(answer)


if __name__ == "__main__":
    main() 
