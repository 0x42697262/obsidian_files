
---
source: https://gist.github.com/miguelmota/c35999dbf9c15154d0aec8dace29d481
---

Make a new file in `/etc/X11/xorg.conf.d/` named `30-touchpad.conf` with this configuration:
```conf
Section "InputClass"
    Identifier "touchpad"
    Driver "libinput"
    MatchIsTouchpad "on"
    Option "Tapping" "on"
    Option "TappingButtonMap" "lmr"
EndSection
```
Then restart XORG.