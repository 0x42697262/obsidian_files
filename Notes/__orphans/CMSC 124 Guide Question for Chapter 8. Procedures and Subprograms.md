Consider this as your guide in preparing your respective topics assigned in this chapter. At the very least, the answers of these questions should be addressed and discussed in your respective assigned topics. Also, you can use this as a measure of how much you are able to gain understanding and mastery of the topics in this chapter.

#### 1. What are the three general characteristics of subprograms?
The three genereal characteristics of subprograms:
- Each program has a single entry point
- Only one subprogram is executed one at a time
- Control always returns to the caller when the subprogram execution terminates

#### 2. Explain the similarities of processes and coroutines.
Processes and coroutines are subprograms that both gets executed and returns to the caller, however coroutines can return to the caller before it finishes executing. 

#### 3. It is possible to have recursive coroutines. That is, coroutine A calls B, then B may later call A instead of resuming A. Explain how this is implemented.


#### 4. What are the modes, the conceptual models of transfer, the advantages, and the disadvantages of pass-by-value, pass-by-result, pass-by-value-result and pass-by-reference parameter-passing methods?
#### 5. Describe the ways that aliases can occur with pass-by-reference parameters.
#### 6. Describe the problem of passing multidimensional arrays as parameters.
#### 7. What are the two issues that arise when subprogram names are parameters?
#### 8. Define shallow and deep binding for referencing environments of subprograms that have been passed as parameters. What are the advantages and disadvantages of a user program building additional definitions for existing operators, as possibly done in Python and C++? Do you think such user-defined operator overloading is good or bad?
#### 9. What are some disadvantages of using pass-by-name parameter?
#### 10. Recursion is costly because it requires a lot of memory. Explain further on this.
#### 11. In languages such as C, explicit exception handling facilities are not provided but instead it allows the sending of an error-handling procedure as a parameter to each procedure that can detect errors that must be handled. What are the disadvantages of such method?
#### 12. Some languages, like Java, provides exception handling facilities for programmers to use. What are the advantages of a language with an exception handler vs other language that have no exception handling facilities?
#### 13. Exception handlers are not explicitly called. They take control when some error occurs. How is control of execution transferred to exception handler?
#### 14. Given the following C program:
```c
swap(a,b)
int a,b;{
	int t;
	printf(“%d %d\n”, a,b);
	t=a;
	a=b;
	b=t;
	printf(“%d %d\n”, a,b);
}
main(){
	int x=10, y=20;
	printf(“%d %d\n”, x,y);
	swap(x,y);
	printf(“%d %d\n”, x,y);
}
```
The program above uses call-by-value. What will be printed by the program above?
