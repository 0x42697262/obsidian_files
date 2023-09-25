Consider this as your guide in preparing your respective topics assigned in this chapter. At the very least, the answers of these questions should be addressed and discussed in your respective assigned topics. Also, you can use this as a measure of how much you are able to gain
understanding and mastery of the topics in this chapter.
#### 1. Define literal, aggregate, function call, conditional expression, constant and variable.
`Literals` A token type value of an identifier.
`Aggregate` A combined group of tokens that forms a composition.
`Function call` An expression that passes control and arguments (when present) to a function.
`Conditional Expression` An expression that evaluates to true or false.
`Constant` A variable that is static (never changing) which is assigned at the time of declaration.
`Variable` A placeholder of values.

#### 2. Several kinds of expressions may be combined in a single expression. Give some examples of an expression where the different kinds of expression are used in one expression.
```c++
int add_op(int a, int b){
	return a + b;
}

int main(){
	int sum = add_op(69, 420);
	return 0;
}
```
The `int sum = add_op(69, 420);` both have an assignment expression and function call expression so technically this line contains multiple expressions (at least two)

#### 3. C allows conditional expression. Can you give an example of conditional expression in C?
```c
int max = (x < y) ? x : y;
```

#### 4. It is easy to convert a postfix expression to infix, and vice versa. Write the postfix and prefix equivalents of the following expressions:
```
-+*ab-cd/ef
ab*cd-+ef/*
```

`-+*ab-cd/ef`
```
Infix:
	((a*b)+(c-d))-(e/f)
Postfix:
	ab*cd-+ef/-
```
`ab*cd-+ef/*`
```
Infix:
	((a*b)+(c-d))*(e/f)
Postfix:
	*+*ab-cd/ef
```

#### 5. Infix, although the most common notation specifically in mathematics, is considered ambiguous while prefix and postfix are not. Why?
It is ambiguous because when there are more than one operators in an expression, it is unclear which is which to gets evaluated first. Like, `a*b/c-4`. It's not clear whether its `a*(b/c)-4`, `(a*b)/(c-4)`, `(a*b)/c-4`, or other more. Prefix and postix are not ambiguous since you can simply evaluate them from left to right or right to left without losing its precedence which provides only one result.

#### 6. Why does precedence and associativity rules eliminate ambiguity from the expression?
This puts a "rank of order" for the operators so that the highest rank gets evaluated first then onto the next lower rank of order.

#### 7. What is the consequence of allowing side effects and not stating in the language definition how the evaluation should proceed?
Confusion to the programmers writing the code when they expect a proper effect but then there's an unexpected side effect that they are not made aware of.

#### 8. What are the possible values that will be printed by the following programs:
```c++

int a=5;

int f1(){
	a=17;
	return(3);
}

int f2(){
	a=f1()+a;
}

main(){
	f2();
	printf(“%d\n”,a);
}
```
What will be printed when the above program is executed? Explain. [^1]

1. `a` is initialized to `5`.
2. Functions `f1()` and `f2()` are initialized but not called.
3. Function `f2()` is called.
4. Inside function `f2()`, function `f1()` is called.
5. Function `f1()` sets `a` to `17`. It is a local scope so the global `a` is not affected. It remain as `5`. Then returns a value of 3.
6. The line `a=f1()+a;` is now `a=3+a;`. Function `f2()` accesses `a` and it's `5`. So, `a=3+5;` which is `a=8`. A local scope.
7. Prints `a` which is `5`.

Other print value can be `20` if the global variable `a` can be changed.

After running the code, the print value is actually `20`.

#### 9. Consider the following C program:
```c++

int f(int *i){
	*i+=5;
}

main(){
	int x=3;
	x=x+f(&x);
	printf(“%d\n”,x);
}
```
What will be printed if operands in main() are evaluated (a) from left to right? (b) from right to left? [^1]

**(a) left to right**
1. `x` init as `3`.
2. `x=x+f(&x);` is now `x=3+f(&x);`. Then, function `f()` is called with the parameter address value of `&x`.
3. Dereferencing `&x`, the `*i` is `3`. Add `5`, then it is 8.
4. So, `x=3+8;` is `11`.
This prints `11`.

**(b) right to left**
1. Function `f()` gets called first then `x` is not `8` instead of `3`. 
2. So, `x=x+8;` and then `x=8+8;` which is `16`.
This prints `16`.

Ah, as expected. It actually outputs the address of the variable, not the values. That is because function `f()` does not return any value. I forgot. I should be expecting that the variable `x` gets modified since it passes the address, it might be the printing that is the issue?

#### 10. Why is short circuit evaluation being implemented in languages?
Performance. Lesser cpu cycles means no more tasks to do. When a subexpression evaluates in an expression evaluates to false, there is no need to perform the other subexpressions. If I were to quote a random text I have read in the past, implementing short circuit evaluation tends to be efficient and also acts similarly as how people thinks. Like, there is no need to continue evaluating if you know at least one of the expression is true or false. Why would you?

Try evaluating this example:[^1]
```c++
#include <iostream>

int main(){
  int a=9,b=4,c=7,d=1,e=3;
  while( (a=1)==1 && (b=2)==3 && (c=3)==3 || (d=4)==4 || (e=5)==7 ){
    std::cout << a << b << c << d << e << std::endl;
    break;
  }
  return 0;
}
```
What do you think is the result?

#### 11. Short circuit evaluation is not always safe. Explain this in terms of the problem created by the code: `(x>y) || (x++>z)` while executing with short circuit evaluation.
If `x>y` is true, then `x++>z` will never get evaluated due to short circuiting. Hence, the `x++` will never be evaluated. If the programmer is expecting that `x++` increments it, then no it won't.
If `x>y` is false, then `x++>z` gets executed and `x++` is incremented.

#### 12. Explain why translation of expressions becomes more efficient when there are more registers available in the target machine.
I think it's because there is more space for the translation to be stored so that makes it much more efficient to translate.

#### 13. Compare the three approaches to generating code for the expression in terms of (a) time needed for the translation and (b) efficiency of the code generated.
I actually don't understand this part.

---

[^1]: Please try to trace and anticipate the outcome on your own, without actually coding this. You are cheating yourself out of a great learning opportunity if you do that. You can run this code after you have manually attempted to trace the output of this.