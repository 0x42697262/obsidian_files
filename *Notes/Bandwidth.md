---
title: Bandwidth
date: 2023-10-04
tags:
  - Computer-Science
  - DataCommunication
  - Networking
---

# Bandwidth

---

The range of frequencies contained in a composite signal is its bandwidth. The bandwidth is normally a difference between two numbers. The bandwidth of a composite signal is the difference between the highest and the lowest frequencies contained in that signal. The bandwidth determines the channel capacity.

> [!NOTE]-
> If a composite signals contains frequencies between 1000 Hz and 5000 Hz, its bandwidth is 4000 Hz (5000 Hz - 1000 Hz).

> [!NOTE]- The bandwidth of periodic and nonperiodic composite signals
> ![[Pasted image 20231004122656.png]]
>
> - the bandwidth of the periodic signal contains all integer frequencies between 1000 and 5000 (1000, 1001, 1002, …)
> - the bandwidth of the nonperiodic signals has the same range, but the frequencies are continuous

> [!NOTE]- Example 1
> If a periodic signal is decomposed into five sine waves with frequencies of 100, 300, 500, 700, and 900 Hz, what is its bandwidth? Draw the spectrum, assuming all components have a maximum amplitude of 10 V.
>
> Solution:
> Let $fh$ be the highest frequency, $f_l$ the lowest frequency, and $B$ the bandwidth. Then,
> $$B=fh-f_l$$ $$B=900 Hz-100 Hz=800 Hz$$
> The spectrum has only five spikes, at 100, 300, 500, 700, and 900 Hz.
> ![[Pasted image 20231004123612.png]]

> [!NOTE]- Example 2
> A periodic signal has a bandwidth of 20 Hz. The highest frequency is 60 Hz. What is the lowest frequency? Draw the spectrum if the signal contains all frequencies of the same amplitude.
>
> Solution:
> Let $fh$ be the highest frequency, $f_l$ the lowest frequency, and $B$ the bandwidth. Then,
> $$B=fh-f_l$$ $$20 Hz=60 Hz-f_l$$ $$f_l=60 Hz-20 Hz=40 Hz$$
> The spectrum contains all integer frequencies.
> ![[Pasted image 20231004124250.png]]

> [!NOTE]- Example 3
> A nonperiodic composite signal has a bandwidth of 200 kHz, with a middle frequency of 140 kHz and peak amplitude of 20 V. The two extreme frequencies have an amplitude of 0. From 0v to the 20v, the spectrum linear increase or decrease. Draw the frequency domain of the signal.
>
> Solution:
> The lowest frequency must be at 40 kHz and the highest at 240 kHz.
> ![[Pasted image 20231004124549.png]]


