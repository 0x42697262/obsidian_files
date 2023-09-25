---
title: Bus Topology
date: 2023-09-26
tags:
  - ComputerScience
  - Networking
---

# Bus Topology

---

```
A bus topology is like a single road where all the houses (computers) are connected. In this setup, a single cable, called the "bus," runs through all the computers. Each computer taps into this cable to send and receive data. It's like cars on a road; they share the same path.
```

A bus topology is a fundamental network topology in which all devices are connected to a single communication channel, known as a "bus." This bus serves as a shared communication medium through which data is transmitted. Devices in a bus topology are typically connected using a drop cable or connector to tap into the main bus.

In Bus Topology...

- it used to be popular for Ethernet LANs
- multipoint vs point-to-point
- one long cable acts as a backbone to link all the devices in a network
- nodes are connected to the bus cable by _drop lines_ and _taps_

`Drop Line`: a connection running between the device and the main cable
`Tap`: a connector that either splices into the main cable or punctures the sheathing of a cable to create a contact with the metallic core

**Advantages**:

1. Ease of installation
2. Less cabling than mesh and star topologies

**Disadvantages**:

1. Limited number of taps and distance between taps
2. Difficult reconnection and fault isolation
3. Difficult to add new devices (designed for optimal efficiency during installation)
4. Signal reflection at the taps can cause degradation in quality (controlled by number of taps and spacing between them)
5. Fault or break in the bus cable stops all transmission (even between devices on the same side of the problem)
