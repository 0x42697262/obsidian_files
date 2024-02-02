---
title: (pwnable.kr) fd
date: 2024-02-02
tags:
  - ctf/pwnablekr
  - file-descriptor
  - c
---

# (pwnable.kr) fd

---

**Contents:**

1. [[#Introduction]]
2. [[#Pre-requisites]]
3. [[#Methodology]]
   1. [[#Enumeration]]
   2. [[#Exploitation]]
4. [[#Documentation of Flags/Proofs]]
5. [[#Conclusion]]
6. [[#Acknowledgments and References]]

---

# Introduction

---

The goal of this Capture The Flag is to print out a `flag` file with no `read` permissions. Basic understanding of C language can solve this challenge within less than a minute. A compiled binary file and its source code is provided.

# Pre-requisites

---

### File Descriptors

POSIX API standards have these following:

| Integer Value | Name            | <unistd.h> symbolic constant | <stdio.h> file stream |
| ------------- | --------------- | ---------------------------- | --------------------- |
| 0             | Standard input  | STDIN_FILENO                 | stdin                 |
| 1             | Standard output | STDOUT_FILENO                | stdout                |
| 2             | Standard error  | STDERR_FILENO                | stderr                |

### atoi()

See `man atoi`.

### Linux File Permissions

```sh
.rw-r--r--
drw-r--r--
lrwxrwxrwx
```

Above is an example file permissions. It's grouped into three parts: _user owner_, _group owner_, and _others_. There are 10 flags. The first flag is the file type (`.` for a file, `d` for a directory, and `l` for symlinks). The remaining ones are permission settings.

Permissions

- `r`: read
- `w`: write
- `x`: execute
- `s`: setuid

If the permission settings flag is set to `-`, then the specific owner does not have the permissions to read, write, and/or execute.

### Connecting with SSH

To play the game, connect to `ssh fd@pwnable.kr -p2222` with `guest` as the password.

# Methodology

---

## Enumeration

Once connected to the SSH session, check the current working directory, the user logged in, and the files.

```sh
fd@pwnable:~$ ls -la
total 40
drwxr-x---   5 root   fd   4096 Oct 26  2016 .
drwxr-xr-x 116 root   root 4096 Oct 30 05:25 ..
d---------   2 root   root 4096 Jun 12  2014 .bash_history
-r-sr-x---   1 fd_pwn fd   7322 Jun 11  2014 fd
-rw-r--r--   1 root   root  418 Jun 11  2014 fd.c
-r--r-----   1 fd_pwn root   50 Jun 11  2014 flag
-rw-------   1 root   root  128 Oct 26  2016 .gdb_history
dr-xr-xr-x   2 root   root 4096 Dec 19  2016 .irssi
drwxr-xr-x   2 root   root 4096 Oct 23  2016 .pwntools-cache


fd@pwnable:~$ pwd
/home/fd

fd@pwnable:~$ id
uid=1002(fd) gid=1002(fd) groups=1002(fd)
```

Found the `flag` file. We can try outputting it.

```sh
fd@pwnable:~$ cat flag
cat: flag: Permission denied
fd@pwnable:~$
```

No permissions to read. The `flag` is owned by `fd_pwn`. Notice that file `fd` has execute permissions for the group `fd`. We can check its file type with `file`.

```sh
fd@pwnable:~$ file fd
fd: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=c5ecc1690866b3bb085d59e87aad26a1e386aaeb, not stripped
```

It's a compiled binary executable. Notice that this file has `s` attribute being set. Which means when this binary gets executed, it will run under the user owner, `fd_pwn`.

I assume that `fd.c` is the source code of `fd` binary.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char buf[32];
int main(int argc, char* argv[], char* envp[]){
	if(argc<2){
		printf("pass argv[1] a number\n");
		return 0;
	}
	int fd = atoi( argv[1] ) - 0x1234;
	int len = 0;
	len = read(fd, buf, 32);
	if(!strcmp("LETMEWIN\n", buf)){
		printf("good job :)\n");
		system("/bin/cat flag");
		exit(0);
	}
	printf("learn about Linux file IO\n");
	return 0;

}
```

## Exploitation

Run `fd` file.

```sh
fd@pwnable:~$ ./fd
pass argv[1] a number

fd@pwnable:~$ ./fd aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
learn about Linux file IO
```

Let's go back to the source code `fd.c`. The first thing that goes to my mind is the string comparison check `strcmp()` against `LETMEWIN`. I assumed that typing `LETMEWIN` as the argument would work but it did not.

```sh
fd@pwnable:~$ ./fd LETMEWIN
learn about Linux file IO
```

An argument must be passed and converted to an integer. After some trial and error, the `atoi()` function converts the argument into value `0`. The hexadecimal value `0x1234` is equivalent to `4660` in decimal format. If the converted integer from `atoi()` is 0, then that must mean `fd` variable is `-4660`. Thus, I tried using `4660` as the argument, not `0x1234`, and this allowed as to execute the `read()` function which normally fails if the file descriptor is not equal to `0`, `1`, or `2`.

At this point, it's as easy as typing the password `LETMEWIN`.

```sh
fd@pwnable:~$ ./fd 4660
LETMEWIN
good job :)
mommy! I think I know what a file descriptor is!!
```

# Documentation of Flags/Proofs

---

Hence, our flag is `mommy! I think I know what a file descriptor is!!`.

# Conclusion

---

This took me about 12 hours to solve and I expected I would do some binary exploitation like stack smashing or buffer overflows but it seems like that's not needed. I misunderstood the purpose of `strcmp()` and I tried doing buffer overflows instead.

```sh
fd@pwnable:~$ ./fd 4660
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcat flag
learn about Linux file IO
fd@pwnable:~$ cat flag
cat: flag: Permission denied
```

Well, yeah, of course it would not work lmao. It took me another half an hour or more to realize that `strcmp()` checks if the input string is equal... Just Wow.

Therefore, to easily win this challenge, you can do the following:

```sh
fd@pwnable:~$ ./fd 4660
LETMEWIN
good job :)
mommy! I think I know what a file descriptor is!!
```

And get the flag ;)

# Acknowledgments and References

---

- https://en.wikipedia.org/wiki/File_descriptor
- manual pages
