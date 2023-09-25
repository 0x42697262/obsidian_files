---
type: note
source: https://wiki.archlinux.org/title/Activating_numlock_on_bootup#SDDM
---

Edit `/etc/sddm.conf` and add:
```conf
[General]
...
Numlock=on
```