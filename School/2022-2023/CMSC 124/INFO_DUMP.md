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
----
Get all sources [here](../../../REFERENCES.md#INFO_DUMP)