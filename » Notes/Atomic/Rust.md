---
title: Rust
date: 2023-12-20
tags:
  - "#programming"
---

# Standard Input

```rust
use std::io;
let mut input: String = String::new();
io::stdin()
	.read_line(&mut input)
	.expect("<expected string error here>");
```