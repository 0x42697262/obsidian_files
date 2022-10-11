>[!INFO]
> Status: #WIP 
> Tags: #CMSC124 #Machine_Problem

----
# Machine Problem 2
No need to make an interpreter ros this MP, however I think that's much better?
More info on BNF [[Backus-Naur Form|here]].

```
Valid strings:
~x+~y
(x+z-y)
z-(x+y)

Invalid strings:
a+b
xy-xz
z(x+y)

-----------------

BNF:
	<expression> ::= <term> | <expression><operator><term>
	<term>       ::= <expression> | (<expression>) | ~(<expression>) | <sign>
	<sign>       ::= <identifier> | ~<identifier>
	<operator>   ::= + | - 
    <identifier> ::= A | B | ... | Z | a | b | ... | z

```

```
Make a BNF for palindrome (without spaces)

Palindrome: pop, pop a pop, a but tuba  
Not a palindrome: hey, joe, the quick brown fox

BNF:
	<palidrome>  ::= <character>
						| <character><character>
						| <character><palidrome><character>
						| <space>
	<space>      ::= ε | ε<palindrome>
	<character>  ::= A | B | ... | Z | a | b | ... | z
```



[[CMSC124 Machine Problem 2|Machine Problem 2]]