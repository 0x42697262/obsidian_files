---
title: NixOS
date: 2024-02-05
tags:
  - nixos
---

# NixOS

---

## Troubleshooting

### Direct firmware load for XXX failed with error -2

Issues with:

- [[rtl88x2bu]] `rtw88/rtw8822b_fw.bin`

> [!NOTE] Solution
> 
> In NixOS configuration, add `hardware.enableAllFirmware = true;`. This is equivalent to installing `linux-firmware` in other distros such as Arch Linux.
>
> Source: https://nixos.org/manual/nixos/stable/#sec-profile-all-hardware


