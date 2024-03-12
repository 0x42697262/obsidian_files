---
title: Cryptography
date: 2024-03-07
tags:
  - computer-security
---

A systematic method of encrypting and decrypting messages or data.
It is used in [[Computer Security]] by protecting [[Data Communications]] and [[Computer Networking]].

Fully integrates [[CIA Triad]], that must be achieved at all cost:

- Confidentiality
- Integrity
- Availability

Cryptography is not limited to encrypting messages where [[Plain Text]] is converted into [[Cipher Text]], but instead a broader concept that involves other processes necessary for securing messages such as [[Encryption]], [[Hashing]], and [[Authentication]].

# History

## Paper Era

A "pen and ink" period.
[[Code]]s in this era is relatively simple because messages had to be decoded by hand.
Not very secure compared to modern standards.

Because of common cipher types [[Substitution Cipher]] and [[Transposition Cipher]].

## Mechanical Era

- [[Enigma machine]]

## Modern Era

Heavy reliance on mathematics and electronic computers.

- [[One-Time Pad]]
- [[Data Encryption Standard]] by [[National Institute for Standards in Technology]]

# Confidentiality, Integrity, and Authenticity

## Confidentiality

The goal is to prevent everyone except the intended entity from reading or tampering a message, known as [[Plain Text]], by transforming the message into an encrypted message, known as a [[Cipher Text]].

If the message is *confidential*, then the attacker does not know its contents.

## Integrity

If the message has *integrity*, then the attacker cannot change its contents without being detected.

## Authenticity

If the message has *authenticity*, then it's guaranteed that the message was written by the entity who claims to have written it.

---

For implementations of techniques, see [[Cryptographic Systems]].