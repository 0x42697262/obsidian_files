---
title: sqlite3
date: 2024-03-09
tags: 
terms:
---

A terminal-based front-end to the SQLite library that can evaluate queries interactively and display  the results in multiple formats.

# Converting from other data type

## csv

```
$ sqlite3 <filename>.db
sqlite3> .mode csv
sqlite3> .import <csv> <db name>
```