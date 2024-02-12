---
title: GNU Debugger — Command Hook
date: 2024-02-11
tags:
  - binary-analysis
  - reverse-engineering
  - debugger
---

# [[GNU Debugger]] — Command Hook

---

Executes commands every time a breakpoint event occurs.

## Usage

Running `define hook-stop` allows to enter commands. To finish, enter `end`.

Example

```
(gdb) define hook-stop
x/1i $eip
x/16wx $esp
end
```