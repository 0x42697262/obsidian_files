no history, check it outside

`BNF Grammar` uses the set of rules or productioin of the form:
```
left-side ::= right-side
```
where `left-side` is a *nonterminal symbol*, `right-side` is a string of nonterminal and terminal symbol

<details>
<summary>Ignore these</summary>

`Terminal` - represents the atomic symbols of the language
`Nonterminal` - represents other symbols as defined to the right of the symbol `::=` (read as "produces" or "is defined as")

`|` - alternative (what??)
`{}` - possible repetitions of the enclosed symbols zero or more time
</details>
```
	A ::= B | {C}
```
"*`A`* produces `B`" or "*`A` produces a string of zero or more `C`'s*"

## Some definitions
`Backus-Naur Form` (BNF) is a notation for expressing a CFG
`grammar` - defines what are legal statements in a language
`alphabet` - finite set of symbols that appear in the language
`nonterminals` - symbols that can be replaced by collections of symbols found in a production
- denoted by surrounding symbol with `<>` ( \<turtle\> )
`terminals` - symbols from the alphabet
`productions` - replacement rules for nonterminals
`start symbol` - the initial symbol from which all sentences in the language can be derive
- `Note: it is usually the left hand side of the first production when a start symbol is not specifically given`
`Alternation`
- denoted by `|` ( bad \<cats\> | good \<dogs\> )
`Replacement`
- denoted by `::=` (the **productions**)
`blanks` - are ignored or must be in some escaping scheme like quotes `""`
`terminals` - unadored symbols


## Writing BNF
Rules
```
<sentence>  ::= <subject> <predicate>
<subject>   ::= <noun> | <article> <noun>
<predicate> ::= <verb> | <verb> <object>
<noun>      ::= man | woman
<article>   ::= the | a
<verb>      ::= runs | walks
<object>    ::= home
```
Construct the sentence, start from the start symbol `<sentence>`
```
sentence ::= <subject> <predicate>
         ::= <article> <noun> <predicate>
         ::= the <noun> <predicate>
         ::= the man <predicate>
         ::= the man <verb> <object>
         ::= the man walks <object>
         ::= the man walks home
```

# Activity
1. Show the derivation of the sentence `The horse jumps overboard.` using the rules:
```
sentence ::= subject predicate
subject ::= noun | article noun
predicate ::= verb | verb object
noun ::= man | horse
article ::= the | a
verb ::= runs | jumps
object ::= overboard | over the fence
```

Solution:
```
<sentence> ::= <subject> <predicate>
           ::= <article> <noun> <predicate>
           ::= the <noun> <predicate>
           ::= the horse <predicate>
           ::= the horse <verb> <object>
           ::= the horse jumps <object>
           ::= the horse jumps overboard
```

2. Show the derivation of the following strings given  the grammar defined.
```
CSI3125
MAT2743
PHY1200
EPI6581
CSI9999
```
Rules:
```
<coursecode>    ::= <acadunit> <coursenumber>  
<acadunit>      ::= <letter> <letter> <letter>  
<coursenumber>  ::= <year> <semesters> <digit> <digit>  
<year>          ::= <ugrad>|<grad>  
<ugrad>         ::= 0 | 1 | 2 | 3 | 4  
<grad>          ::= 5 | 6 | 7 | 9  
<semesters>     ::= <onesemester>|<twosemesters>  
<onesemester>   ::= <frenchone>|<englishone>| <bilingual>  
<frenchone>     ::= 5 | 7  
<englishone>    ::= 1 | 3  
<bilingual>     ::= 9  
<twosemesters>  ::= <frenchtwo> | <englishtwo>  
<frenchtwo>     ::= 6 | 8  
<englishtwo>    ::= 2 | 4  
<digit>         ::= 0|1|2|3|4|5|6|7|8|9  
<letter>        ::= A|B|...|Z
```

Solution:
```
CSI3125
	<coursecode> ::= <acadunit> <coursenumber>
				 ::= <letter> <letter> <letter> <coursenumber>
				 ::= C <letter> <letter> <coursenumber>
				 ::= CS <letter> <coursenumber>
				 ::= CSI <coursenumber>
				 ::= CSI <year> <semesters> <digit> <digit>
				 ::= CSI <ugrad> <semesters> <digit> <digit>
				 ::= CSI3 <semesters> <digit> <digit>
				 ::= CSI3 <onesemester> <digit> <digit>
				 ::= CSI3 <englishone> <digit> <digit>
				 ::= CSI31 <digit> <digit>
				 ::= CSI312 <digit>
				 ::= CSI3125

MAT2743
	<coursecode> ::= <acadunit> <coursenumber>
				 ::= <letter> <letter> <letter> <coursenumber>
				 ::= M <letter> <letter> <coursenumber>
				 ::= MA <letter> <coursenumber>
				 ::= MAT <coursenumber>
				 ::= MAT <year> <semesters> <digit> <digit>
				 ::= MAT <ugrad> <semesters> <digit> <digit>
				 ::= MAT2 <semesters> <digit> <digit>
				 ::= MAT2 <onesemester> <digit> <digit>
				 ::= MAT2 <frenchone> <digit> <digit>
				 ::= MAT27 <digit> <digit>
				 ::= MAT274 <digit>
				 ::= MAT2743
				 
PHY1200
	<coursecode> ::= <acadunit> <coursenumber>
				 ::= <letter> <letter> <letter> <coursenumber>
				 ::= P <letter> <letter> <coursenumber>
				 ::= PH <letter> <coursenumber>
				 ::= PHY <coursenumber>
				 ::= PHY <year> <semesters> <digit> <digit>
				 ::= PHY <year> <semesters> <digit> <digit>
				 ::= PHY <ugrad> <semesters> <digit> <digit>
				 ::= PHY1 <semesters> <digit> <digit>
				 ::= PHY1 <twosemesters> <digit> <digit>
				 ::= PHY1 <englishtwo> <digit> <digit>
				 ::= PHY12 <digit> <digit>
				 ::= PHY120 <digit>
				 ::= PHY1200
				 
EPI6581
	<coursecode> ::= <acadunit> <coursenumber>
				 ::= <letter> <letter> <letter> <coursenumber>
				 ::= E <letter> <letter> <coursenumber>
				 ::= EP <letter> <coursenumber>
				 ::= EPI <coursenumber>
				 ::= EPI <year> <semesters> <digit> <digit>
				 ::= EPI <grad> <semesters> <digit> <digit>
				 ::= EPI6 <semesters> <digit> <digit>
				 ::= EPI6 <onesemester> <digit> <digit>
				 ::= EPI6 <frenchone> <digit> <digit>
				 ::= EPI65 <digit> <digit>
				 ::= EPI658 <digit>
				 ::= EPI6581
				 
CSI9999
	<coursecode> ::= <acadunit> <coursenumber>
				 ::= <letter> <letter> <letter> <coursenumber>
				 ::= C <letter> <letter> <coursenumber>
				 ::= CS <letter> <coursenumber>
				 ::= CSI <coursenumber>
				 ::= CSI <year> <semesters> <digit> <digit>
				 ::= CSI <grad> <semesters> <digit> <digit>
				 ::= CSI9 <semesters> <digit> <digit>	
				 ::= CSI9 <onesemester> <digit> <digit>	
				 ::= CSI9 <bilingual> <digit> <digit>	
				 ::= CSI99 <digit> <digit>
				 ::= CSI999<digit>
				 ::= CSI9999
```


---
Get all sources [here](../../REFERENCES.md#Backus-Naur%20Form)
