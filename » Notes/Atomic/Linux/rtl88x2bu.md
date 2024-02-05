---
title: rtl88x2bu
date: 2024-02-05
tags:
  - linux
  - drivers
  - chipset
  - wifi
---

# rtl88x2bu

---

## Issues

### Direct firmware load for rtw88/rtw8822b_fw.bin failed with error -2

```bash
$ dmesg | grep rtw 

[   11.489416] rtw_8822bu 1-8:1.0: Direct firmware load for rtw88/rtw8822b_fw.bin failed with error -2
[   11.489420] rtw_8822bu 1-8:1.0: failed to request firmware
[   11.841049] rtw_8822bu 1-8:1.0: failed to load firmware
[   11.841052] rtw_8822bu 1-8:1.0: failed to setup chip efuse info
[   11.841053] rtw_8822bu 1-8:1.0: failed to setup chip information
[   11.841098] rtw_8822bu: probe of 1-8:1.0 failed with error -22
[   11.841120] usbcore: registered new interface driver rtw_8822bu
```

Fix available here [[NixOS#Direct firmware load for XXX failed with error -2]].