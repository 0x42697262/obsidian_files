2023-03-26

---

**CaptureTheFlag:** 
>picoCTF 2023

**Challenge Name:** 
>Special

**Challenge Description:** 
>Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM) Start your instance to see connection details.
>
>Additional details will be available after launching your challenge instance.

**Challenge Category:** 
>General Skills

**Challenge Points:** 
>300

---

### Intro
It has been a week since I last solved a challenge for this competition and I just opened the challenge because I procrastinated my assignments. After reading the description, I had few thoughts like the spell checking of this challenge can automatically call a command that it was not supposed. But after running the challenge instance, I was wrong lol. It took me almost 30 minutes to solve this challenge.

### TL;DR Solution
1. `~/../../bin/cat */*`

---
### How I solved the challenge
After logging through the ssh session, I was greeted with a prompt then I proceed to type the command `ls` and see if it worked but it got autocorrected instead.
```sh
Special$ ls
Is 
sh: 1: Is: not found
```
Notice that `l` turned into letter `I` and from there I tried other commands.
```sh
Special$ cd
Ad 
sh: 1: Ad: not found
Special$ CD
Ad 
sh: 1: Ad: not found
Special$ mkdir
Media 
sh: 1: Media: not found
Special$ rm
Am 
```
That did not seem to work. A thought came, *what if i just print the alias?*
```sh
Special$ alias
Alias 
sh: 1: Alias: not found
Special$ type
Type 
sh: 1: Type: not found
```
And that still did not work lmao. I went to type random non-alphabetic characters like `.`, `;`, `&`, etc. while combining it with other commands. And it turns out the result is still the same. Until I accidentally hit the return key `Enter` and got this error:
```sh
Special$ 
Traceback (most recent call last):
  File "/usr/local/Special.py", line 19, in <module>
    elif cmd[0] == '/':
IndexError: string index out of range
Connection to saturn.picoctf.net closed.
```
And I was surprised, I thought maybe I can take advantage of that? But nope, that did not work so I just continued and went on running other syntaxes.
```sh
Special$ /
Absolutely not paths like that, please!
Special$ ~
~ 
sh: 1: /home/ctf-player: Permission denied
Special$ ~/
I 
sh: 1: I: not found
Special$ ~
~ 
sh: 1: /home/ctf-player: Permission denied
Special$ ~~
I 
sh: 1: I: not found
Special$ //
Absolutely not paths like that, please!
Special$ ////
Absolutely not paths like that, please!
Special$ /.
Absolutely not paths like that, please!
Special$  /
/ 
sh: 1: /: Permission denied
```
Eh, no results. I tried running `pwd` but that just got autocorrected into another string. At here on, I thought *what if I just combine the commands and it will eventually return a password based on the syntax?* yeah no that did not work.
```sh
Special$ @@
I 
sh: 1: I: not found
Special$ pico@
Pico 
sh: 1: Pico: not found
Special$ picoctf{@@}
Picoctf{@@} 
sh: 1: Picoctf{@@}: not found
Special$ picoctf{@@@
Picoctf{@@@ 
sh: 1: Picoctf{@@@: not found
Special$ @@@@@@
@@@@@@ 
sh: 1: @@@@@@: not found
Special$ ls@
Is 
sh: 1: Is: not found
Special$ l@
La 
```
At this point, I was about to give up until I read about `cat` that uses `<` or was it the `>` so I tried that as well but no luck. The next one was putting the syntax inside the `$()` and see if it works...
```sh
Special$ $(pwd)
$(pwd) 
sh: 1: /home/ctf-player: Permission denied
Special$ $(ls)
$(ls) 
sh: 1: a: not found
Special$ ls
Is 
sh: 1: Is: not found
Special$ `ls`
Also 
sh: 1: Also: not found
Special$ `pwd`
`pwd` 
```
Still no luck. I really wanted to know the current working directory but I just can't seem to figure out. I even tried calling other shells like `zsh`, `fish`, `bash`, etc. but got this result instead.
```sh
Special$ ssh
Why go back to an inferior shell?
Special$ bash
Why go back to an inferior shell?
Special$ zsh
Why go back to an inferior shell?
Special$ fish
Why go back to an inferior shell?
Special$ shell
Why go back to an inferior shell?
```

I just need to know the current working directory. Really... Not until I realized rather than just directly calling `pwd` command, what if I just call it through absolute path? Well, that would not work since absolute paths are not allowed. But what works is relative paths... So I had this idea.
```sh
Special$ /bin/ls
Absolutely not paths like that, please!
Special$ ~/../../../bin/ls
~/../../../bin/ls 
blargh
```
Hmm... what is `blargh`? A text? A directory? I don't know. So, I assumed it's a directory and just tried to `cd` into it but lol `/bin/cd` does not exist haha. Rather than doing that, I continued to push what I wanted to do at first.
```sh
Special$ ~/../../bin/cd blargh
~/../../bin/cd large 
sh: 1: /home/ctf-player/../../bin/cd: not found
Special$ ~/../../../../bin/pwd
~/../../../../bin/pwd 
/home/ctf-player
```
And that's how I got my current directory. I know where I am, that means the password is not in the root directory, right? Yep, after some manuevering of commands, I finally found the flag.
```sh
Special$ ~/../../../../bin/pwd
~/../../../../bin/pwd 
/home/ctf-player
Special$ ~/../../../../bin/cat blargh
~/../../../../bin/cat large 
/home/ctf-player/../../../../bin/cat: large: No such file or directory
Special$ ~/../../../../bin/cat *
~/../../../../bin/cat * 
/home/ctf-player/../../../../bin/cat: blargh: Is a directory
Special$ ~/../../../../bin/ls *
~/../../../../bin/ls * 
flag.txt
Special$ ~/../../../../bin/cat */*
~/../../../../bin/cat */* 
picoCTF{5p311ch3ck_15_7h3_w0r57_b741d1b1}Special$ Connection to saturn.picoctf.net closed by remote host.
Connection to saturn.picoctf.net closed.
```
The flag is `picoCTF{5p311ch3ck_15_7h3_w0r57_b741d1b1}`.

---
**Notes:**
I had some assumptions that the spell check only works for the first letter and the spell checks is sort of like a regex but that was not the case.

Notice that I did not cat the `blargh` since it gets converted into `large` so instead of using words, I used a **regex** `*` instead. It worked.

For this challenge that's worth 300 points, this does not seem to be worth to be 300 points imo. Sure, I had a hard time figuring the spell checker out but it's not really that difficult.