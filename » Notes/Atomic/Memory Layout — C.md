---
title: Memory Layout — C
date: 2024-01-25
tags:
  - memory-allocation
  - CMSC134
---

The memory layout is arranged in a long array the size of memory bytes as its elements. Each element is one byte.

Left most element has the address `0x00000000` and the right most element has the address `0xFFFFFFFF`.

![[Memory_Layouts_—_C.1.png]]

But this is difficult to read, thus the layout is drawn in a *grid form*. The bottom-left element has the address `0x00000000` and the top-right element has the address `0xFFFFFFFF`. 

- Each row is 4 bytes, hence each grid cell element is 1 byte

Addresses increases when moving from left to right and bottom to top.

![[Memory_Layouts_—_C.2.png]]

This does not change the actual layout in the memory since we are only drawing this for the sake of easier reading.

> [!NOTE]
> As an example, we are dealing with $2^{32}$ bytes of memory. Hence why the maximum address is `0xFFFFFFFF`.
> This would be different for a memory with $2^{64}$ bytes.

Each [[Memory Addresses|address space]] is divided into four [[Memory Addresses#Sections|sections]].