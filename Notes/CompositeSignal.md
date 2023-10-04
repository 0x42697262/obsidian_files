---
title: Composite Signal
date: 2023-10-04
tags:
  - Physics
---

# Composite Signal

---

A composite signal is made of many simple [[SineWave|sine waves]]. In the early 1900s, French mathematician Jean-Baptiste Fourier showed that any composite signal is actually a combination of simple sine waves with different frequencies, amplitudes, and phases Fourier analysis).

A composite signal can be periodic or nonperiodic.

- **periodic composite signal**: can be decomposed into a series of simple sine waves with discrete frequencies that have integer values (1, 2, 3, and so on)
- **non-periodic composite signal**: can be decomposed into a combination of an infinite number of simple sine waves with continuous frequencies that have real values

> [!NOTE]- Example 1
> This figure shows a periodic composite signal with frequency $f$. This type of signal is not typical of those found in data communications. We can consider it to be three alarm systems, each with a different frequency. The analysis of this signal can give us a good understanding of how to decompose signals.
> ![[Pasted image 20231004101414.png]]

> [!INFO]- Decomposition of a composite periodic signal in the time and frequency domains
> ![[Pasted image 20231004101601.png]]
> 
> - the amplitude of the sine wave with frequency $f$ is almost the same as the peak amplitude of the composite signal.
> - the amplitude of the size wave with frequency $3f$ is one-third of that of the first, and one with $9f$ is one-ninth of the first
> - the frequency of the sine wave with frequency $f$ is the same as the frequency of the composite signal; it is called the _fundamental frequency_, or _first harmonic_
> - the sine wave with frequency $3f$ has a frequency of 3 times the fundamental frequency; it is called the _third harmonic_
> - the third sine wave with frequency $9f$ has a frequency of 9 times the fundamental frequency; it is called the _ninth harmonic_
> - note that the frequency decomposition of the signal is discrete

> [!INFO]- Example 2
> This figure shows a nonperiodic composite signal. It can be the signal created by a microphone or a telephone set when a word or two is pronounced. In this case, the composite signal cannot be periodic, because that implies that we are repeating the same word or words with exactly the same tone. Human voice frequency is between 0Hz and 4kHz.
> ![[Pasted image 20231004102436.png]]
> 
> - in a time-domain, there are an infinite number of simple sine frequencies
> - although number of frequencies in a human voice is infinite, the range is limited
> - normal human being create continuous range from 0 and 4 kHz
> - frequency decomposition of the signal yields a continuous curve
> - infinite number of frequencies between 0.0 and 4000.0
> - to find amplitude related to frequency $J$, we draw a vertical line at $f$ to intersect the envelope curve
> - height of vertical line is the amplitude of frequency
