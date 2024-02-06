---
title: Stack
date: 2024-01-25
tags:
  - data-structure
  - "#CMSC134"
---

# Stack

---

A [[Data Structure]] with contiguous block of memory containing data. Adding and removing data will always be performed at the last data placed[^1].

The top of the stack is a [[Stack Pointer]] [[Register]] whose address dynamically changes at runtime by the [[Kernel]].

## Example

```
╔═══════════════╗
║       c       ║ ⟵ top of the stack (stack pointer)
╠═══════════════╣
║       b       ║
╠═══════════════╣
║       a       ║ ⟵ bottom of the stack
╚═══════════════╝
```

---

[^1]: [[Last In First Out]]
