>z [!INFO]
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
    <expression> ::= <term> 
    <term>       ::= <factor> 
					| <term><operator><term>
					| ~(<term><operator><term>)
					| (<term><operator><term>)
    <factor>     ::= <identifier> | ~<identifier>
    <operator>   ::= + | - 
    <identifier> ::= x | y | za

	<expression> ::= <term> | <negate>
	<negate>     ::= ~<expression> | ~<identifier>
	<operator>   ::= + | - 
    <identifier> ::= x | y | z

------------------

Tests:

<factor><operator><term>
<negation><operator><term>
~<identifier><operator><term>
~x<operator><term>
~x+<term>
~x+<factor>
~x+<negation>
~x+~<identifier>
~x+~y

<factor><operator><term>
<negation><operator><term>
~<identifier><operator><term>
~x<operator><term>
~x+<term>
~x+<term><operator><factor>
~x+<factor><operator><factor>
~x+<identifier><operator><factor>
~x+y<operator><factor>
~x+y-<factor>
~x+y-<negation>
~x+y-~<identifier>
~x+y-~z

I need to make a test case for parenthesis.
```