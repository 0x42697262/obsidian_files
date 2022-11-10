> [!INFO]
> Status: #WIP
> Tags: #Machine_Problem #CMSC142 #Python

----
# CMSC 142 May the for be with you - version 1
~~what to put here soon for future notes... ofc the code~~

```python
def main():
    lines = int(input())
    expression = str()
    for _ in range(lines):
        expression += input()
```

Input Example:
```c++
3
if (x<4){
	x++;
}
```

Output:
```c++
if (x<4){    x++;}
```
We need to parse this.

# BNF Grammar?
```bnf
<expression>  ::=  <type><variable>
<variable>    ::=  <identifier><assignment><_next>
<assignment>  ::=  =<value> | ε
<_next>       ::=  ; | ,<variable>
<type>        ::=  int | float | char | string | bool | void
<identifier>  ::=  [a-zA-Z] [a-zA-Z0-9_]*
<value>       ::= <arithmetic_expression>
```
Source for `<identifier>`: https://mc-stan.org/docs/2_22/reference-manual/bnf-grammars.html

This should read simple statements like:
```c++
int x = 10, y = 8, z = -2;
x = x + y; 
```

Do we really need to tokenize it properly? What if just take the string input up until `;`? Then count the T(n)'s? Since we assume that the input is correct.
In this case take this expression and consume the first `;`:
```c++
int x = 10, y = 8, z = -2;x = x + y;y = x - y;x = x - y;z = x + y;
```
`int x = 10, y = 8, z = -2;` T(n) = 3
`x = x + y;` T(n) = 2
`y = x - y;` T(n) = 2
`x = x - y;` T(n) = 2
`z = x + y;` T(n) = 2

T(n) = 11

As for the `for-loop`, maybe a different approach would be needed. Like, check the keyword `for`, then `statement`, then the scope `{}`, and even include if `else` if the `if-else` exist.

```rust
for(int i=0; i<n; i++){
sum += i;
}
```
If splitting it by `;`, then the result would be `['for(int i=0', ' i<n', ' i++){sum += i', '}']`.

This looks annoying so parse it line by line instead. Just like how it's intended...