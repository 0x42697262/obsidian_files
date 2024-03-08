---
title: CIA Triad
date: 2024-01-26
tags:
  - information-security
  - computer-security
  - information-risk-management
---

A foundation principle for [[Information Security]] that guides the design and implementation of security measures to protect information, and as a comprehensive strategy that includes policies and [[Security Control]]s to minimize [[Cyber Threat]]s.
Provides a framework for understanding and implementing security measure such as [[Cryptography]].

Three Principles:

1. [[#Data Confidentiality Confidentiality|Confidentiality]]
2. [[#Data Integrity Integrity|Integrity]]
3. [[#Data Availability Availability|Availability]]

---

These three principles should prevent [[Threat Actor]]s from unauthorized access or control to private data.

# [[Data Confidentiality|Confidentiality]]

A property where adversaries, or entities that are not authorized access or modify information, from reading our data.
Information should not be disclosed without authorization.

The goal is to prevent everyone except the intended entity from reading or tampering a message, known as [[Plain Text]], by transforming the message into an encrypted message, known as a [[Cipher Text]].

If the message is *confidential*, then the attacker does not know its contents.

# [[Data Integrity|Integrity]]

A property that prevents entities from tampering with our private data.
Maintenance of, and assurance of, accuracy and consistency (completeness and trustworthiness) of data over its life-cycle.

If the message has *integrity*, then the attacker cannot change its contents without being detected.

# [[Data Availability|Availability]] or Authenticity

A property that determines the origin of a given message. 
Information should only be accessible and usable to the authorized entities.

If the message has *authenticity*, then it's guaranteed that the message was written by the entity who claims to have written it.

---
