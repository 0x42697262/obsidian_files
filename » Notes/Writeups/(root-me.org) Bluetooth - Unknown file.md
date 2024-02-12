---
title: (root-me.org) Bluetooth - Unknown file
date: 2023-11-21
tags:
  - ctf/root-me
  - packet-capture-analysis
---

# (root-me.org) Bluetooth - Unknown file

---

## Details

The answer is the sha-1 hash of the concatenation of the MAC address (uppercase) and the name of the phone.

`AB:CD:EF:12:34:56myPhone` -> `023cc433c380c2618ed961000a681f1d4c44f8f1`

## Solution

This is a BT Snoop File Format. 

```
00000000: 6274 736e 6f6f 7000 0000 0001 0000 03ea  btsnoop.........
```

- `6274 736e 6f6f 7000`: btsnoop
- `0000 0001`: Version 1
- `0000 03ea`: Datalink Type of HCI UART (H4)

```
00000010: 0000 000d 0000 000d 0000 0003 0000 0000  ................
00000020: 00e2 2982 2994 18cb                      ..).)..O...
```

Just use Wireshark at this point... 
## Thoughts

This is taking longer than I thought I would expect. I gave up midway and instead used Wireshark like what others did in the forum. However, I did not expect that the MAC address is reversed since I already found the device name. I assumed that the address is besides the device name and I was correct. Except that when I used `sha1sum` to hash the address and device name, I got the wrong result since the address is supposed to be reversed.

---

- https://www.root-me.org/en/Challenges/Network/Bluetooth-Unknown-file
- https://fte.com/webhelpII/HSU/Content/Technical_Information/BT_Snoop_File_Format.htm