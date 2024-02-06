---
title: systemd-analyze — blame
date: 2023-12-25
tags:
  - linux
  - systemd
---

# systemd-analyze — blame

---

List all running units ordered by time initialized. I use this for checking which unit takes the longest to initialize.

command: `systemd-analyze blame`