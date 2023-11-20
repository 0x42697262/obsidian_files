---
title: (root-me.org) TELNET - authentication
date: 2023-11-20
tags:
  - "#ctf/root-me"
  - "#networking/security"
  - "#packet-capture-analysis"
---

# (root-me.org) TELNET - authentication

---

## Description

A [[TELNET]] network packet file needs to be analyzed as [[Capture The Flag|CTF]]. The goal is to find the password.

## Solution

[[TELNET]] sends the password requests one character of the user password at a time. I thought the method would be similar to a [[File Transfer Protocol]]. To solve this challenge, I used [[Wireshark]] as a tool to filter the packet data with `telnet.data` and then find the frames that contains `Data: Password:` until we find `Data: \r`. I was able to acquire the password by manually checking each frames after filtering the data. This is still an **inefficient** method.

 A better approach of this would be to open up [[Wireshark]] and right click the first frame of a [[TELNET]] frame request then select `Follow -> TCP Stream`. The result looks like this:

```
........... ..!.."..'.....#..%..%........... ..!..".."........P. ....".....b........b.... B.

........................"......'.....#..&..&..$..&..&..$.. .....#.....'........... .9600,9600....#.bam.zing.org:0.0....'..DISPLAY.bam.zing.org:0.0......xterm-color.............!.............."............

OpenBSD/i386 (oof) (ttyp1)

  

login: .."........"ffaakkee

.

Password:<PASSWORD>

.

Last login: Thu Dec 2 21:32:59 on ttyp1 from bam.zing.org

Warning: no Kerberos tickets issued.

OpenBSD 2.6-beta (OOF) #4: Tue Oct 12 20:42:32 CDT 1999

  

Welcome to OpenBSD: The proactively secure Unix-like operating system.

  

Please use the sendbug(1) utility to report bugs in the system.

Before reporting a bug, please try to reproduce it with the latest

version of the code. With bug reports, please try to ensure that

enough information to reproduce the problem is enclosed, and if a

known fix for it exists, include that as well.

  

$ llss

.

$ llss --aa

.

. .. .cshrc .login .mailrc .profile .rhosts

$ //ssbbiinn//ppiinngg wwwwww..yyaahhoooo..ccoomm

.

PING www.yahoo.com (204.71.200.74): 56 data bytes

64 bytes from 204.71.200.74: icmp_seq=0 ttl=239 time=73.569 ms

64 bytes from 204.71.200.74: icmp_seq=1 ttl=239 time=71.099 ms

64 bytes from 204.71.200.74: icmp_seq=2 ttl=239 time=68.728 ms

64 bytes from 204.71.200.74: icmp_seq=3 ttl=239 time=73.122 ms

64 bytes from 204.71.200.74: icmp_seq=4 ttl=239 time=71.276 ms

64 bytes from 204.71.200.74: icmp_seq=5 ttl=239 time=75.831 ms

64 bytes from 204.71.200.74: icmp_seq=6 ttl=239 time=70.101 ms

64 bytes from 204.71.200.74: icmp_seq=7 ttl=239 time=74.528 ms

64 bytes from 204.71.200.74: icmp_seq=9 ttl=239 time=74.514 ms

64 bytes from 204.71.200.74: icmp_seq=10 ttl=239 time=75.188 ms

64 bytes from 204.71.200.74: icmp_seq=11 ttl=239 time=72.925 ms

...^C

.--- www.yahoo.com ping statistics ---

13 packets transmitted, 11 packets received, 15% packet loss

round-trip min/avg/max = 68.728/72.807/75.831 ms

$ eexxiitt

.
```

## Thoughts

I don't know how [[TELNET]] protocol works so I looked it up and found out that you cannot easily filter the password in `TShark`. Each character key inputs are sent one at a time which is weird in terms of modern standards. I didn't know that the server would echo back the character input to you except the password. If someone wants to filter out the password, maybe they can create a python script that would look for `Data: Login: ` and `Data: Password: ` to acquire the credentials. Enter key is `Data: \r`.

---

- https://www.root-me.org/en/Challenges/Network/TELNET-authentication
- https://www.bvkmohan.com/2017/03/telnet-protocol-analysis.html