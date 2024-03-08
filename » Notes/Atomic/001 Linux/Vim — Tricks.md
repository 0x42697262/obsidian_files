---
title: Vim — Tricks
date: 2024-03-08
tags:
  - vim
terms:
---

# Using as a hex editor with [[xxd]]

Open a binary file and run `:%!xxd`, then edit the hex values as is.
Do `:%!xxd -r` to revert into text mode.
