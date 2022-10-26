CMSC 124 Problem Set 4
**Topic Coverage**: Lexical and Syntax Analysis 

---

### 1. Why is BNF considered advantageous over using an informal syntax description?
BNF is consistent to use across all sorts of grammar when applicable since unlike informal syntax description, hence the reason why BNF descriptions are clear and concise. This makes it easy for humans and software systems to analyze. Since syntax analyzers can be based directly from BNF, it would also be easy to implement and maintain the syntax analyzer.

### 2. Describe the three approaches to building a lexical analyzer. Which of those approaches are most commonly used, and why?
In order to build a lexical analyzer, we must consider three appoaches. These are:
1. Writing a formal description or grammar rules
2. Designing a state diagram describing the token patterns through implementation
3. Designing a state diagram describing the token patterns through hand-construction

When writing the rules for the lexical analyzer, we must consider the token patterns of the language that we can use for the lexical analyzer. This can be done by using a tool called `lex`. The next approach is by designing a state diagram that describes the token patterns which is done through writing a program that implements the diagram. And the other approach, which is similar to the previous approach, follows the same except that it is hand-constructing a table-driven implementation of the state diagram.

The first approach is commonly used amongst the approaches that were mentioned because one can simply write their own tool in building the lexical analyzer or by using existing tools that can automate the process unlike the other two approaches where it is difficult to attain due to its complexity as state diagrams must transition from a state to another.

### 3. Describe the complexity of parsing algorithms. What is the parsing problem, and why is it considered a problem?
Parsing algorithm runs at O(n<sup>3</sup>) which is very slow since the parser traverses recursively and there is a frequent amount of times that goes back and reparse the input once again. When it comes to parsing, there can be two kinds, one that works for any unambiguous grammars and one that works specifically for one unambiguous grammar. The former is complex and inefficient that is why it runs at O(n<sup>3</sup>) and the latter can run at O(n) or linear time which is not fast however it is within an acceptable speeds. The `n` refers to the length of the input.
There are two kinds of parsing algorithms for recursive-decent parsing, these are top-down algorithm and bottom-up algorithm. The former has problems with the leftmost derivation because the grammar can potentially create an infinite loop which will never stop. This can be fixed by converting the grammar without the looping nonterminal. The latter has problems with finding the proper RHS. If there are more than one derivation steps, then it would be complex to execute which is why we need to simplify the grammar.

### 4. What is a left recursion? Why is it not possible to have a grammar having a left recursion as a basis for a top-down parser, and how can this be corrected?
In a grammar, left recursion is when the nonterminal LHS is the starting point of the RHS. Top-down parses cannot use left recursion because the parser would first call the subprogram that can lead into infinite loops. Thsi can be corrected by converting the left recursive grammar into a right recursive grammar through left factoring.

### 5. Describe the purpose of a parse stack in an LR parser.



## References
*Programming Language Concepts*. Georgia State University. Retrieved October 26, 2022, from https://tinman.cs.gsu.edu/~raj/4330/slides/c04.pdf. 
