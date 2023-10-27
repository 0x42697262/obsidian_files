---
title: Data link layer
date: 2023-10-27
tags:
---

# Data link layer

---

- Layer 2 in the [[Open systems interconnection model|OSI Model]]
- Transforms the physical layer, a raw transmission facility, to a link responsible for node-to-node (hop-to-hop) communication

---
## Specific Responsibilities of the Data Link Layer
1. **Framing** - It divides the stream of bits received from the network layer into manageable data units called *frames*.
2. **Addressing** - It adds a header to the frame to define the addresses of the sender and receiver of the frame.
3. **Flow Control** - If the rate at which the data are absorbed by the receiver is less than the rate at which data are produced in the sender, the data link layer imposes a flow control mechanism to avoid overwhelming the receiver.
4. **Error Control** - It adds reliability to the physical layer by adding mechanisms to detect and retransmit damaged, duplicate, or lost frames.
5. **Media Access Control** - When two or more devices are connected to the same link, data link layer protocols are necessary to determine which device has control over the link at any given time.