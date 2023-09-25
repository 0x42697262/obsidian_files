CMSC 124 Problem Set 3  
**Topic Coverage**: Primitive Data Types

----
### 1. A Boolean data type is either true or false. Hence, it can basically be implemented using  only 1 bit. However, some PLs uses more than 1 bit in implementing Boolean values.  What are the arguments for and against representing Boolean values as single bits in  memory?
Some programming languages implement booleans as one bit in order to save space in the memory. However, others are against in using booleans as bits because they are a lot slower to access. A has a register for bytes and words, but not for bits.


### 2. Why do some PLs treat string as a primitive type while others treat it as a composite type? 
Strings are simply a sequence of characters thus other programming languages treats them as composite type while others treat them as primitive types.

### 3. Given the following Pascal code:
```pascal
procedure one;
	var i: integer;
	begin
		...
		i:=0;
		...
		i:=i+1;
		...
	end
```
List three binding occurrences and the time they are performed
1. `var i: integer` (binding at translation time, static) 
2. `i:=0` (binding at translation time, static)
3. `i:i+1` (binding at execution time, dynamic)

### 4. Give one consequence of static type binding and dynamic type binding in terms of type checking. Also, give at least two differences of dynamic from static type binding.
Static Type binding happens at translation time or compile time while Dynamic Type binding happens during execution time or runtime. For static binding, it has specific data types that it can be only be assigned with so that no other data types can be used, which increases the reliability of the programming language. For dynamic binding, the object can have any data type depending on the assigned data, and this decreases the reliability and slows down the execution of the programming language.

### 5. Is widening conversion always safe? If not, state at least one instance showing that it is not safe.
It is always safe as the narrow data is a subset of the wider data. So, there is no loss of data when the conversion process occurs.

### 6. How does the coercion rules weaken the beneficial effect of strong typing?
Since type coercion implicitly converts data to type to another data type, this already breaks the benefits of strong typing. Also, type coercion can be inconsistent when it is not handled properly by the programming language.