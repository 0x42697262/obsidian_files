import unittest
import mp3_recursive_descent_parser_1

par = mp3_recursive_descent_parser_1.Parser()

class TestRDP(unittest.TestCase):
    def test_grammar_true(self):
        self.assertEqual(True, par.parse("1-2*3$"))
        self.assertEqual(True, par.parse("(1-2)*(3+1)$"))
        self.assertEqual(True, par.parse("2/3$"))
        self.assertEqual(True, par.parse("(1-2)+(2-3)*(1/1)$"))
        self.assertEqual(True, par.parse("((1)+1)$"))
        self.assertEqual(True, par.parse("(((1*1*1*1*1-1-2-3-1/1/1*1+1)))$"))
        self.assertEqual(True, par.parse("(1)+(2)*(3)$"))
        self.assertEqual(True, par.parse("(1-3-2-1-3-1-2+(1-2-3-1-2/1*2+3+(1+2*3-1/2*3+1*2/3)+(1-2*3/1+2/3+(1/2*3+1/2*3))))$"))
        self.assertEqual(True, par.parse("(1)$"))

    def test_grammar_false(self):
        self.assertEqual(False, par.parse("12-32$"))
        self.assertEqual(False, par.parse("(($))$"))
        self.assertEqual(False, par.parse("$$"))
        self.assertEqual(False, par.parse("22-3$"))
        self.assertEqual(False, par.parse("(4-1)*3$"))
        self.assertEqual(False, par.parse("3/$"))
        self.assertEqual(False, par.parse("$$$"))
        self.assertEqual(False, par.parse("2$$"))
        self.assertEqual(False, par.parse("2+2$+2"))
        self.assertEqual(False, par.parse("(((3+2$)))$"))
        self.assertEqual(False, par.parse("(1)+(1)$$"))
        self.assertEqual(False, par.parse("(1)*(1-1-2$)"))
        self.assertEqual(False, par.parse("((((())))))$"))
        self.assertEqual(False, par.parse("1)$"))
        self.assertEqual(False, par.parse("+1)$"))
        self.assertEqual(False, par.parse("1)"))
        self.assertEqual(False, par.parse("(1)"))
        self.assertEqual(False, par.parse("(($"))



if __name__ == "__main__":
    unittest.main()
