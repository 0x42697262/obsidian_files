Consider this as your guide in preparing your respective topics assigned in this chapter. At the very least, the answers of these questions should be addressed and discussed in your respective assigned topics. Also, you can use this as a measure of how much you are able to gain understanding and mastery of the topics in this chapter.

#### 1. MODULA-2 uses the elseif alternative to nesting for two-way selectors. That is, it uses the statement whose syntax is:
```modula2
if expression then statement1
elseif expression then statement2
else statement3
```
Explain the problem with the use of this syntax.

If there are multiple branching involved (more than 2), then you can use `elsif` for modula-2. So, instead of having to nest `if-else` statements, one can simply branch other conditional statements.
Example:
```modula2
IF expr1 THEN stmt1
ELSE
	IF expr2 THEN stmt2
	else 
		IF expr3 THEN stmt3
		ELSE stmt0
```
Can be written as:
```modula2
IF expr1 THEN stmt1
ELSIF expr2 THEN stmt2
ELSIF expr3 THEN stmt3
ELSE stmt0
```

#### 2. Given the concurrent Pascal program:
```pascal
program increment;
const m=20;
var n: integer;
	procedure increase;
	begin
		for i:=1 to m do n:=n+1;
	end;
begin
	n:=0;
	cobegin
		increase; increase;
	coend
	writeln(“The sum is ‘,n);
end.
```
What will be the possible output of this program?

Probably `The sum is 40`, assuming that the syntax is correct.

#### 3. What is the difference in semantics between the case statement in Pascal and the switch statement in C?
Both C and Pascal breaks out of the case when a match is found, and both the languages follows a "check every cases until a match is found". Instead of using `else` for C language just like in Pascal, C uses `default` instead. Both languages are almost the same except their syntaxes although in order to write multiple instructions for Pascal, there is a need to wrap the instructions around `begin` and `end` unlike in C which just uses `{}`.

#### 4. What is wrong with arithmetic IF statement of FORTRAN?

#### 5. Give the equivalent case statement in Pascal for the FORTRAN if statement:
```fortran
IF (expression) label1, label2, label3.
```

#### 6. Rewrite the following C for loop
```c
for (sum=0, i=0, j=0; i<10; i++, j+=2)
	sum+=i+j;
```
in the loop statements in Java, Python and FORTRAN.

#### 7. Describe the seven kinds of statements in terms of C. Or, classify all the C statements into one of the seven major classifications of statements.

#### 8. Differentiate ADA’s exit statements from C’s break statements.

#### 9. Enumerate several design issues involved in the design of conditional and iterative statements.

#### 10. Some programming languages have a single syntax for statements. Give examples of programming languages that adopt this strategy.

#### 11. Although the use of templates for translating statements are very popular, it also has its disadvantages. What are these disadvantages?