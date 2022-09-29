To start `picom` on a terminal after killing it: 
```
picom --experimental-backends &; disown
```
`disown` is for making sure `picom` is still alive after the terminal dies