"""
BNF:
	<palindrome>  ::= aa | bb | cc | ... | zz |
	   	            a<palindrome>a | b<palindrome>b | c<palindrome>c | ... | z<palindrome>z |
	   	            <character> 
	<character>  ::= a | b | ... | z |
"""

class Parser():
    def __init__(self, bnf: str, start_symbol: str):
        self._bnf = bnf
        self._terms = dict()
        self._terms["START_SYMBOL"] = start_symbol

    def list_terms(self, bnf) -> list:
        lines = bnf.strip().split('\n')
        for l in range(len(lines)):
            lines[l] = (lines[l].replace(' ', ''))
        
        return lines

    def prepare_production(self):
        for non_term in self._bnf:
            _ = non_term.split("::=")
            self._terms[_[0]] = _[1].split("|")

    def return_bnf(self) -> dict:
        return self._terms

    def start(self):
        self._bnf = self.list_terms(self._bnf)
        self.prepare_production()

class BNF_Interpreter():
    def __init__(self, bnf: list):
        self._bnf = bnf

    def verify(self, expression: str) -> bool:
        str_expr = list(expression.replace(' ', ''))
        
        while len(str_expr) > 1:
            if str_expr.pop() != str_expr.pop(0):
                return False

        return True

    def ui(self, expr: str):
        print(f"{expr}: {self.verify(expr)}")


def main():
    bnf = "<palindrome>  ::= aa | bb | cc | dd | ee | ff | gg | hh | ii | jj | kk | ll|mm|nn|oo|pp|qq|rr|ss|tt|uu|vv|ww|xx|yy|zz| a<palindrome>a | b<palindrome>b | c<palindrome>c | d<palindrome>d | e<palindrome>e | f<palindrome>f | g<palindrome>g | h<palindrome>h | i<palindrome>i| j<palindrome>j| k<palindrome>k| l<palindrome>l|m<palindrome>m| n<palindrome>n| o<palindrome>o| p<palindrome>p| q<palindrome>q| r<palindrome>r| s<palindrome>s| t<palindrome>t| u<palindrome>u| v<palindrome>v| w<palindrome>w| x<palindrome>x| y<palindrome>y| z<palindrome>z | <character>\n"
    bnf += "<character>  ::= a | b | c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y | z |\n"

    parse = Parser(bnf, "<palidrome>")
    parse.start()
    validate = BNF_Interpreter(parse.return_bnf())
    validate.ui("pop")
    validate.ui("pop a pop")
    validate.ui("a but tuba")
    validate.ui("hey")
    validate.ui("joe")
    validate.ui("the quick )brown fox")
    validate.ui("awf fwa ")

    validate.ui(input("Enter Test Case: "))


if __name__ == "__main__":
    main()
