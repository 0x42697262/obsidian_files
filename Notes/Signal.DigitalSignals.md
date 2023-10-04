---
title: Digital Signals
date: 2023-10-04
tags:
  - ComputerScience
  - DataCommunication
  - Networking
---

# Digital Signals

---

In addition to being represented by an analog signal, information can also be represented by a digital signal. For example, a $1$ can be encoded as a positive voltage and a $0$ as zero voltage. A digital signal can have more than two levels.

In this case, we can send more than 1 bit for each level.

> [!NOTE]- Two digital signals: one with two signal levels and the other with four signal levels
> This figure shows two signals, one with two levels and the other with four.
> ![[Pasted image 20231004125023.png]]
>
> We send 1 bit per level in part (a) of the figure
> and 2 bits per level in part (b) of the figure. In general, if a signal has $L$ levels, each level needs $log_2L$ bits.

> [!NOTE]- Example 1
> A digital signal has eight levels. How many bits are needed per level? We calculate the number of bits from the formula:
> Number of bits per level = $log_28=3$
>
> Each signal level is represented by 3 bits.

> [!NOTE]- Example 2
> A digital signal has nine levels. How many bits are needed per level?
> 
> We calculate the number of bits by using the formula. Each signal level is represented by 3.17 bits. However, this answer is not realistic. The number of bits sent per level needs to be an integer as well as a power of $2$. For this example, 4 bits can represent one level.


