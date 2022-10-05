# 1. What is Programming Language
- used to communicate
- in natural language, both are persons
- in programming language, computer and user
- describes computation
- communicates an instructions to a computer by a person to execute tasks
- commands formed by user executed by the computer

# 2. History of Programming Languages  
- no computers however theoritical studies exists to express computations so maths is used
- `Plankalkul` 1st documented programming language... is that true
- `Fortran` 1st successful programming language... oh? designed specifically for scientific and engineering
- ... more programming languages here but meh

# 3. Programming Language Paradigm  
### Classifications of Languages by Wegner
1.  Imperative
2. Declarative

- pattern or modeling and solving problems
- basically the style or way of programming of how we think of problems and solve them

### Paradigms
1. Imperative
	- Explicit
	- Computation is performed in sequences in the RAM
	- Procedural Programming Paradigm
	- Focuses more on the steps in acquiring results
	- **Types**
		1. [Block-structured](INFO_DUMP.md#Block-Structured)
		2. [Object-based](INFO_DUMP.md#Object-Based)
		3. [Distributed Programming](INFO_DUMP.md#Distributed%20Programming)

2. Declarative
	- Implicit
	- Computations must be specified
	- Considered as higher level concept than imperative languages
	- Requires the specification of a relation or function
	- Logical Programming Paradigm
	- Focuses more on the end result rather than the steps
	- **Types**
		1. [Logic Programming](INFO_DUMP.md#Logic%20Programming)
		2. [Functional Languages](INFO_DUMP.md#Functional%20Languages)
		3. [Database Languages](INFO_DUMP.md#)

3. Structured
4. Procedural
5. Functional
	- Control flow is expressed by combining function calls, rather than by assigning values to variables

6. Function-level
7. Object-oriented
	- Sending messages to objects
	- Object responds to messages performing operations (methods)

8. Event-driven
9. Flow-driven
10. Logic
11. Constraint
12. Aspect-oriented
13. Reflective
14. Array

Note that programs can have multiple paradigms.

### Applications of Programming Languages
- **Scientific Computations**
	- FORTRAN
	- Algol-60
	- Algol-68
- **Data Processing**
	- COBOL
- **Artificial Intelligence**
	- Lisp
	- Prolog
- **Text Processing**
	- SNOBOL
	- ICON
- **System Programming**
	- C
	- ADA
	- Modula
- **General Purpose**
	- PL/I
	- Pascal

# 4. Generations of Programming Language  
## 1st Generation Languages
- All low level languages (machine and assembly languages)

## 2nd Generation Languages
- Languages designed during the early 60's (Algol-60, BASIC, COBOL, FORTRAN)

## 3rd Generation Languages
- High-level languages perfected around the late 60's
- Procedural (imperative paradigm)
	- PL/I
	- Pascal
	- Modula-2
	- C
	- ADA
- Functional
	- Lisp
	- APL
	- ML
- Logic
	- Prolog
- Object-oriented
	- C++
	- Objective-C
	- Smalltalk
	- Objective Pascal
	- Eiffel
	- ADA-95
	- Java

## 4th Generation Languages
- [Domain Specific](DEFINITIONS.md#Domain-specific%20language) 
- **Visual Programming environment**
	- VB
	- Delphi
	- Visual Age
	- Visual C++
- **Database**
	- Natural
	- SQL
	- Acess
	- FoxPro
	- dBase
	- AdaBase
- **Expert System Shells**
	- OPS5
	- EMYCIN
	- CLIPS
	- EXSYS
- **SPREADSHEET**
	- Excel
	- OpenOffice Calc
	- Quattro Pro
	- Lotus 1-2-3

## 5th Generation Languages
- Has visual tools to assist in coding (IDEs)
- Example
	- Mercury
	- OPS5
	- Prolog

- Low Level
	- 1st gen
	- 2nd gen
- High Level
	- 3rd gen
	- 4th gen
	- 5th gen
	- pokemon


# 5. Language Evaluation Criteria  
From a user's point of view: `Readability`, `Writability`, `Reliability`, `Cost`

**What makes a good language?**
- Clarity, simplicity, and unity
- Naturalness for the application
- Support of abstraction
- Ease of program verification
- Programming environment
- Portability of programs
- Cost of use

**What makes a language successful?**
- Expressive power
- Ease of use for the novice
- Ease of implementation
- Open source (heh)
- Excellent compilers
- Economics, patronage, and inertia

| CHARACTERISTIC          | READABILITY | WRITABILITY | RELIABILITY |
|-------------------------|:-----------:|:-----------:|:-----------:|
| Simplicity              |•            |•            |•            |
| Orthogonality           |•            |•            |•            |
| Data types              |•            |•            |•            |
| Syntax design           |•            |•            |•            |
| Support for abstraction |             |•            |•            |
| Expressivity            |             |•            |•            |
| Type checking           |             |             |•            |
| Exception handling      |             |             |•            |
| Restricted aliasing     |             |             |•            |



## Readability
- The ease which programs can be read and understood early programming languages were constructed for computers instead of users in mind
- `One of the most important criteria for judging a programming language is the ease with which programs can be read and understood.`

<details>
<summary>A bit of history?</summary>
<li>Before 1970, software development was largely thought of in terms of writing code.</li>
<li>The primary positive characteristic of programming languages was efficiency.</li>
<li>Language constructs were designed more from the point of view of the computer than of the computer users.</li>
</details>
- **Readability must be considered in the context of the `problem domain`**

- **Characteristics**
	- `overall simplicity` of a programming language strongly affects its readability
	- 


## Writability
- Writability is a measure of how easily a language can be used to create programs for a chosen problem domain
<details>
	 <summary>Own Thoughts</summary>
	 I think a measuring criteria on how easy for a language to write programs for a given solution
</details> 
- Characteristics that affects Readability also affects Writability because the developer needs to reread their code.

_writability must be considered in the context of the target problem domain of a language._ 
`It is simply not reasonable to compare the writability of two languages in the realm of a particular application when one was designed for that application and the other was not.`

- **Characteristics**
1. Simplicity & Orthogonality
	- 

2. Support for Abstraction
- **Programming languages can support two distinct categories of abstraction**:
	1. process
	2. data

3. Expressitivity



## Evaluation Criteria of Programming Languages
- `Portability` - the ease with which programs can be moved from one implementation to another
- `Generality` - the applicability to a wide range of application
- `Well-definedness` - completeness and precision of the language's official definition
- `Hierarchical decomposition`
- `Modular decomposition`
- `Sequencing`
- `Data manipulation`
- `Redundancy`

# 6. Levels of Programming Languages  
From lowest level to highest: `Machine language` -> `Assembly language` -> `High-level language`

# 7. Methods of Implementation
There are two methods: [Compilation](INFO_DUMP.md#Compilation) and [Interpretation](INFO_DUMP.md#Interpretation)

## Syntax, Semantics, and Pragmatics
`Syntax` - written form of a program
`Semantics` - meaning given to the various syntactic constructs, i.e., how these constructs behave when executed by a computer.
`Pragmatics` - history and some implementation methodology specific to that language

----
Get the [references](REFERENCES.md#Background%20and%20Preliminaries%20Lecture%20Slides) here.