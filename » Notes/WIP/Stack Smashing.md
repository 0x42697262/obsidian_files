---
title: Stack Smashing
date: 2024-02-06
tags:
  - buffer-overflow
  - "#CMSC134"
  - stack-overflow
---

# Stack Smashing

---

A [[Cyberattack]] that causes a [[Stack Overflow]]. This is done by intentionally **overwriting** the [[Buffer]] on the [[Call Stack]]. This is a type of [[Stack]]-based [[Buffer Overflow]] vulnerability.

- It is an old technique.
- Mitigated by [[Buffer Overflow Protections]].

## Concept

When written in memory unsafe languages like C and C++, memory allocations does not have bounding checks[^1]. This means that when a buffer is allocated, there is no built-in mechanism to prevent writing data beyond the intended size of the buffer. An attacker can exploit this vulnerability by overflowing the buffer, causing it to overwrite adjacent memory regions. 


We can then write specific [[Shellcode]]s which gets executed by the [[Extended Instruction Pointer]].
```not my own words
By carefully crafting the input data, the attacker can overwrite critical data structures, such as the return address on the stack, with a malicious payload known as "shellcode". When the vulnerable program attempts to return from the function, it will unwittingly transfer control to the injected shellcode, allowing the attacker to execute arbitrary commands or gain unauthorized access to the system
``` 

A debugger like [[GNU Debugger]] can be used to inspect the memory address of the vulnerable program.

# Methodology

---

[^1]: [[Bounds Checking]]