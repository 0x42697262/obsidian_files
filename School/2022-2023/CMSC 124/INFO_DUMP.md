# Block-Structured
- Procedure is the principal building block of the program
- State of computation is represented by the stack with active procedure at the top
- No restrictions on duplicate items on the stack, thus recursions are allowed
- Blocks consist of one or more declarations and statements. A programming language that permits the creation of blocks, including blocks nested within other blocks, is called a block-structured programming language. Blocks are fundamental to structured programming, where control structures are formed from blocks.<sup>[source](https://en.wikipedia.org/wiki/Block_(programming))</sup>

### Examples
- Algol-60
- Algol-68
- Pascal
- C
- Fortran
- ADA

----

# Object-Based
`Object` - a group of procedure that shares a state (or data)
- All data and procedures that apply to the data are captured in a single object
- btw this is basically object-oriented programming (OOP) if you didn't notice

### Examples
- packages of ADA
- modules of Modula
- objects of Smalltalk

----

# Distributed Programming
- Languages for [loosely coupled systems](../../DEFINITIONS.md#Loose%20Coupling)
- Does not need memory sharing since they have their own memory and processors
- Can avoid some problems on resolving memory conflicts

---
# Logic Programming
- Based on subset of predicate calculus
- Composed of a series of axioms or facts, rules of inference, and a theorem or query to be proved
- logic program defines a search space of problem reductions that can solve all instances of the desired goal

### Examples
- Prolog
- (please add more examples here)

---
# Functional Languages
- Operates only through functions which returns one value provided by a parameter
- A program is a functional call with parameters which involve a call to a function to produce the value of a parameter
- Functions can be considered as values that can be passed to another function
- A functional program defines a system of rewriting rules that can evaluate a desired function

### Examples
- Lisp
- (add more, onegai)

----
# Compilation
- method where a high-level language is translated into another implemented language (like assembly or machine language)
- Produce the machine language equivalent of the high-level language, wherein machine language is the one that is ultimately executed
- SPEEEED
`Compiler` - translator which is also a program running in the intended computer

----
# Interpretation
- Simulates through a program running on another host computer, a computer whose machine language is the high-level language
- makes your life easier... *yay, scripting*!

# Syntax and Semantics
## Character Set
- set of symbols used
	- all characters that can be used in writing, inputs, and outputs (to the program)
	- Example:
		- Machine Language (0 and 1)
		- Algol-60 (alphanumeric characters and 52 other special characters = 114)
		- FORTRAN (47 characters)
		- COBOL (51 characters)
		- PL/I (60 characters)
	- modern languages uses ASCII

## Identifiers
- strings used to name data objects, procedures, keywords
	- has rules to consider
	
## Operator Symbols
- represents primitive operations

## Keywords and Reserved Words
- `Keyword` - identifier used as a fixed part of the syntax
- `Reserved Words` - a potentially restricted keyword in usage

## Comments and Noise Words
- `Comments` - ignored during translations
- `Noise Words` - optional words included in a statement
	- you can remove a word without affecting its syntax and the execution is still the same

## Delimeters and Bracket
- marks beginning and end of syntactic construct

## Free-Field Format and Fix-Field Format
- `Free-Field Format` - allows program statements to be written anywhere
- `Fixed-Field Format` - have certain rules or position in writing program code

## Expressions
- basic syntactic element
- indicate conditions
- evaluate variable values
- 3 forms:
	- prefix
	- postfix
	- infix

## Statements
- Formats:
	- Single Basic Statement
	- Different syntax for each statement type

## Overall Program-Subprogram Structure
what? hello i need more info here, not examples ~~im just lazy~~


## Abstract Syntax
- preferred by language designers who study the formal aspect of programming languages
- simple listing of all possible forms for each of the syntactic classes in the language
- gives the components of each language construct
	- leaves out representation details
- appropriate for normal manipulation of programs

*pls check abstract syntax of pascal, thanks (not here, but on the internet)*

## Concrete Syntax
- preferred by language implementers
- detects whether a string is a well-formed string in the language or not
- **Expressing Concrete Syntax**
	- [Backus-Naur Form](./Week%203-4/Backus-Naur%20Form.md)
	- Syntax Diagrams
	- Context-Free Grammars

----
Get all sources [here](../../../REFERENCES.md#INFO_DUMP)