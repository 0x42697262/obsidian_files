---
title: GNU Debugger
date: 2024-02-11
tags:
  - binary-analysis
  - reverse-engineering
  - debugger
---

- [[GNU Debugger — set|set]]
- [[GNU Debugger — hook-stop|hook-stop]]

# Usage

## Debugging A Program

### From a File

```sh
gdb <elf executable>
```

### From a Process

```sh
gdb -p <process id>
```

To find the process id, run `ps aux | grep <filename>`.

> [!NOTE]
>
> This might need [[sudo]].