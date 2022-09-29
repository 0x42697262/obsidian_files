## 1. Give the basic difference between a declarative and imperative language. Then, classify the following as either imperative or declarative.
Imperative Language is an explicitly defined language where computations are performed as sequences in RAM that focuses more on the teps in acquiring a result hence why it is a procedural programming paradigm. Declarative Language is an explicity defined language which focuses more on the result. It is a type of logical programming paradigm that is considered as a higher level of concept.

| Language  |     Classification      |
| --------- |:-----------------------:|
| FORTRAN   | Imperative<sup>1</sup>  |
| Algol-60  | Imperative<sup>2</sup>  |
| Lisp      | Declarative<sup>3</sup> |
| COBOL     | Imperative<sup>4</sup>  |
| APL       | Declarative<sup>5</sup> |
| SNOBOL    | Imperative<sup>6</sup>  |
| BASIC     |       Imperative        |
| Algol-W   |       Imperative        |
| Jovial    |       Imperative        |
| PL/I      |       Imperative        |
| SIMULA-67 |       Imperative        | 
| Algol-68  |       Imperative        |
| Pascal    | Imperative<sup>7</sup>  |
| C         | Imperative<sup>7</sup>  |
| Prolog    | Declarative<sup>7</sup> |
| Smalltalk |       Imperative        |
| Modula-2  | Imperative<sup>8</sup>  |
| ADA       | Imperative<sup>7</sup>  |
| C++       | Imperative<sup>7</sup>  |
| Java      | Imperative<sup>7</sup>  |


## 2. A programming language may be block-structured, object-based and distributive. How is this possible?
Both block-structured and object-based programming are a part of the structured programming paradigm, and I think each structure or components of written codes are capable of running as one system.


## 3. A programming language may be logic-based, but it cannot be functional. Why so?
Logic-based programming are derived from facts and relations and compute the based on a set of provided rules whereas functional programming can rewrite rules to however you want to compute the desired data. Thus, logic-based programming cannot be functional due to how it operates although functional programming can be logic-based.

## 4. When writabilty is enhances, readability suffers. Explain.
There are multiple characteristics that affects writability, in this case it would be abstraction and expressivity. When there's too much of an abstraction, it can create confusion you to the developer or the person reading the code who is not familiar with the language. When there is too much expressivity, it would also make the code confusing to read. A famous example of this would be the incrementation in C/C++ which is `count++` and `++count`. Sure, they both increment one value however each has its own meaning. These increase the writability but this also affects readability to some extent. <sup>[9]</sup>


## 5. Give some advantages of compilation over interpretation and vice versa. Considering all  these, why is compilation a preferred method of implementation over interpretation?
**Advantages of Compilation**:
1. Better performance due to optimized code
2. Works specifically for the hardware since the language is translated into machine language
3. Highly reliable since the program is design for the specific hardware
 
**Advantages of Interpretation:**
1. Program can run on any hardware as long as there is an interpreter
2. Easier to implement and maintain
3. Easier to learn thus it is very useful for scripting

Compilation is preferred since the code can be optimized specifically for the hardware thus increasing its efficiency. This also makes it easier to implement code for system hardware unlike interpreted language where everything is execute at runtime. Since compilation does not need to simulate the code like the interpreter, compiled programs can execute as fast as it can. <sup>[9]</sup>


## 6. Interpretive programs are slower to execute than compiled programs. Explain why.
Interpretive programs must first gets executed by the interpreter before being executed by the hardware. This adds time to the execution, and since interpretive programs need to be run on every system, it has to be reliable on every possible scenario it is on. Compiled programs are simply different as they do not need to be simulated by an interpreter since the program is translated into machine language where the compiled code is executed directly from the hardware level.


## 7. Compiled programs require more time during program development than interpretive programs. Why is this so?
I do not think compiled programs take more time to write than interpretive programs since it depends on how good language can be. An interpretive program can also be compiled if you choose to do so.
However, the only time compiled programs would take longer than interpretive programs in development is the compilation time as it would take a lot of computing power to translate the code into machine language. Basing this on experience of compiling WINE, Firefox, almost Gentoo, and certain open source software.


## 8. How does the overall simplicity of a programming language affect its readability?
Three reasons, the `large number of constructs` that the programmers would prefer learning the subset of language to ignore the language's features, `feature multiplicity` wherein there are more than one method in writing a particular operation, and `operator overloading` where an operator can have different meanings and implementations. <sup>[9]</sup>


## 9. Why does too much orthogonality cause problems? Why is it considered a detrimental  effect to writability?
Having too much orthogonality increases complexity of the programming language since it is a combination of primitive constructs then if it were to allow each combination to be legal and meaningful, the programming language might allow absurd constructs since there are no restrictions thus allowing extremely complex constructs. Rather than having a single programming language, it will not considered as one due to its unnecessary complexity.


## 10. Java uses a right brace to mark the end of all compound statements. What are the arguments  for and against this design?
This makes Java use lesser reserved keywords for their design however this reduces the simplicity and increases the complexity of the language as it will be harder to read the written code. On a nested structure, right braces results to a very confusing spaghetti code. <sup>[9]</sup>


## 11. Some programming languages (e.g. Pascal) uses the semicolon to separate statements,  while Java uses it to terminate statements. Which of these, in your opinion, is most natural and least likely to result in syntax errors? Support your answer.
Since I've coded with a terminate statement language like C/C++ in the past, I have gotten used to `;` being a terminate statement rather than a separate statement. Since in terminate statement, the `;` acts like a period `.` if it were in an English sentence. As for separating statement, `;` acts like a comma `,`.  Thus, I think that terminate statement would result to lesser syntax errors because there is a simple rule to consider: it terminates your statement and it is almost everywhere.
Although others would find separate statement easier to read, I find it easier to remember when to end, especially if there are multiple statements present.


## 12. Many contemporary languages allow two kinds of comments: one in which delimiters are used on both ends (multiple-line comments) and one in which a delimiter marks only the beginning of the comment (one-line comments). Discuss the advantages and disadvantages of each of these with respect to the language evaluation criteria.
One-line comments makes it easier to read for simple notes for a specific statement of a code. Since it's easy to read it is also easy to write. However, when you need to write multiple lines comments, one-line comments tends to be annoying to write thus it is why we need multiple-line comments. Multiple-line comments makes it easier for us to read and write for a specific block of code thus increasing its reliability. One-line comment does not increase its reliability since it is possible for a one-line comment to get lost in the sea of lines of statements.
If you need something simple, one-line comments works best since it can easily be read and written, and it is reliable only for a block structure. Adding multiple one-line comments to a block structure would make the readability of the comments complex thus decreasing its reliablity.
If you need something that incorporates the entire block structure, multiple-line comment works the best as it only needs a few syntax to write and it can easily be read hence why it got good reliability. However, do not use it for simple syntaxes since one-line comment exsists. Why would you use multiple-line comment instead of one-line comment?

----
# References
[1] *The Fortran Programming Language — Fortran Programming Language*. (n.d.). Retrieved September 16, 2022, from https://fortran-lang.org/en/
[2] *An Interview with FRIEDRICH L. BAUER*. (1987, February 16). Retrived September 16, 2022, from http://www.algol60.org/history/interviewBauer.pdf
[3] _A Brief Introduction to Lisp_. (n.d.). Retrieved September 16, 2022, from https://courses.cs.vt.edu/%7Ecs1104/TowerOfBabel/LISP/Lisp.outline.html
[4] _What is COBOL? | Micro Focus_. (n.d.). Retrieved September 16, 2022, from https://www.microfocus.com/en-us/what-is/cobol
[5] _APL Wiki_. (n.d.). Retrieved September 16, 2022, from https://aplwiki.com/
[6] _SNOBOL4 Resources_. (n.d.). Retrieved September 16, 2022, from https://www.regressive.org/snobol4/
[7] _Programming Languages and Paradigms_. (n.d.). Retrieved September 16, 2022, from https://icarus.cs.weber.edu/~dab/cs1410/textbook/1.Basics/programs.html
[8] Schlegel, C. (n.d.). _Free Modula-2 Pages: Home_. Retrieved September 16, 2022, from https://freepages.modula2.org/
[9]  Harrykar. (2018). “Software Development | Language Evaluation Criteria.” Retrieved September 17, 2022, from:  https://progr-harrykar.blogspot.com/2018/11/language-evaluation-criteria.html  