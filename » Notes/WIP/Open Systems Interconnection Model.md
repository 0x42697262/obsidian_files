---
title: Open Systems Interconnection Model
date: 2023-09-26
tags:
  - computer-networking/models
---

# Open Systems Interconnection Model

---

OSI Model is a conceptual framework used to describe the functions of a [[Computer Networking|networking system]].

The purpose of OSI model is to show how to facilitate communication between different systems without requiring changes to the logic of the underlying hardware and software. This allows communication between all types of computer systems.

## Layers

1. [[Physical Layer|Physical Layer]]
2. [[Data Link Layer|Data Link Layer]]
3. [[OpenSystemsInterconnectionModel.NetworkLayer|Network Layer]]
4. [[OpenSystemsInterconnectionModel.TransportLayer|Transport Layer]]
5. [[OpenSystemsInterconnectionModel.SessionLayer|Session Layer]]
6. [[OpenSystemsInterconnectionModel.PresentationLayer|Presentation Layer]]
7. [[OpenSystemsInterconnectionModel.ApplicationLayer|Application Layer]]

**User Support Layers**: allow interoperability among unrelated software systems
**Transport Support Layers**: links two subgroups and ensures that what the lower layers have transmitted is in a form that the upper layers can use
**Network Support Layers**: deal with the physical aspects of moving data from one device to another (such as electrical specifications, physical connections, physical addressing, and transport timing and reliability)

An exchange using the OSI model:
![[OSI Model — exchange.png]]

- descending, sequential
- data unit, packet
- header or trailer
- electromagnetic signal (electrical/optical)
- digital form
- encapsulation

## History

- Established in 1957 by International Standards Organization
- A layered model that dominated data communications and networking literature before 1990, which was then replace by TCP/IP
