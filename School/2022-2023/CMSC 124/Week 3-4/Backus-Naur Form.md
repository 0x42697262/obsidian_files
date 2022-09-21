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

```
<sentence> ::= <subject> <predicate>
           ::= <article> <noun> <predicate>
           ::= the <noun> <predicate>
           ::= the horse <predicate>
           ::= the horse <verb> <object>
           ::= the horse jumps <object>
           ::= the horse jumps overboard
```


---
Get all sources [here](../../REFERENCES.md#Backus-Naur%20Form)
