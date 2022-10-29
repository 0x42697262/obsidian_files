> [!INFO]
> Status:
> Tags: #Linux

----
# Stream Editor
### Edit a line variable
```bash
sed -i 's/<var>=.*/<var>=<string>' <file>`
```
Example, we have a file and we wanted to edit the variable `Inherits`.
```conf
[Icon Theme]
Inherits=Koishi
```
We can do this by `sed -i 's/Inherits=.*/Inherits=Patchouli' file.conf`.
`-i` specifies the input. Without this, *sed* will only output the string. *See manpages for sed*
`.*` regular expression for all characters except line break (the `.`)
`s` substitute the string