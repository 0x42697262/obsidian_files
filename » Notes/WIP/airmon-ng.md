---
title: airmon-ng
date: 2023-12-25
tags:
  - wifi
---

# airmon-ng

---

## Monitor Mode

### Starting [[Monitor Mode]]

> [!Note]
> Make sure to kill [[NetworkManager]] and [[wpa_supplicant]] before running monitor mode.
> 
> For more than one wifi adapters, one interface can be used for connecting to the internet while the others can be used for [[Monitor Mode]].

`airmon-ng start <interface>`

Use [[iwconfig]] to verify if monitor mode has been set. *Note this does not verify if monitor mode is working.*

## Checking and Killing Interfaces

To check, `airmon-ng check`. To kill, `airmon-ng check kill`.

This will kill all the processes that handles network configuration. To only kill one process, use [[systemctl]] to stop the processes.