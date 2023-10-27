---
title: Star network topology
date: 2023-09-26
tags:
  - Computer-Science
  - DataCommunication
  - Networking
---

# Star network topology

---

>[!INFO]
>![[Star network topology.png]]

```
Imagine you have a group of friends, and you all want to chat with each other. In a star topology, one friend, let's call them the "hub," is at the center. Instead of everyone talking directly to each other, they all talk to the hub. The hub then passes on the messages to the right friend. It's like having a group chat where all messages go through one person before reaching others.
```

A type of network configuration where all nodes (devices) are connected to a central node, often referred to as a "hub" or "switch".

Each node has a dedicated point-to-point connection with the hub/switch.

In Star Topology...

- it is usually used in [[DataCommunication.Networking.LocalAreaNetwork|Local Area Network]]
- each node have a dedicated point-to-point link only to a central controller (hub)
- devices are not directly linked to one another
- the controller acts as an exchange

**Advantages**:

1. Less expensive than [[Mesh network topology|mesh]]
2. Needs only one link and one I/O port to connect
3. Easy to install and reconfigure
4. Additions, moves and deletions involve only one connection
5. Robust
6. Easy fault identification and fault isolation (as long as hub is working - used to monitor problems)

**Disadvantages**:

1. Dependency on one single point - the hub
2. More cabling than in other topologies (such as ring or bus)
