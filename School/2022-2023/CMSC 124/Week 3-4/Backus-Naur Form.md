no history, check it outside

`BNF Grammar` uses the set of rules or productioin of the form:
```
left-side ::= right-side
```
where `left-side` is a *nonterminal symbol*, `right-side` is a string of nonterminal and terminal symbol

`Terminal` - represents the atomic symbols of the language
`Nonterminal` - represents other symbols as defined to the right of the symbol `::=` (read as "produces" or "is defined as")

`|` - alternative (what??)
`{}` - possible repetitions of the enclosed symbols zero or more time
```
	A ::= B | {C}
```
"*`A`* produces `B`" or "*`A` produces a string of zero or more `C`'s*"

