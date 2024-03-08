---
title: GNU Compiler Collection
date: 2024-02-10
tags:
  - compiler
  - gcc
  - c
  - cpp
---

*aka GCC*


# Compilation

## Disable [[Stack Smashing]]

```sh
gcc -fno-stack-protector
```

## Output Preprocessor

```sh
gcc -E -P <source code>
```

## Assembly Code Generated from Compilation Phase

```sh
gcc -S -masm=intel <source code>
```

This should create an assembly file with `.s` as extension.

## Generate Object File

```sh
gcc -c <source code>
```

This should create an assembly file with `.c` as extension. To confirm, run `file <object file>` and this should output:

```
<filename>.o: ELF 64-bit LSB relocatable, x86-64, version 1 (SYSV), not stripped
```

---

For [[Debugging]], see [[GNU Debugger]].