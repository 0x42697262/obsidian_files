---
title: (root-me.org) FTP - authentication
date: 2023-11-20
tags:
  - ctf/root-me
  - "networking/security"
  - "packet-capture-analysis"
---

# (root-me.org) FTP - authentication

---

## Description

A `.pcap` file is provided as a challenge. The goal is to analyze and _find the password_ in the packets that contains File Transfer Protocol network logs.

## Solution

Opened Wireshark and manually inspected each entries line by line. It is not an **efficient** method of doing it. I first analyzed it by packet length. But I did not find anything. So I went ahead to investigate the packets one by one until I found an FTP request that submits a password to the server. The **password** can be found on **packet #11**.

A better approach to solving this is to use TShark to analyze the network traffic.
Better approach: `tshark -r <packet file> -Y 'ftp.request.filter == PASS'` and the output should be something like this:

```sh
11   7.639420 10.20.144.150 → 10.20.144.151 FTP 81 Request: PASS <PASSWORD>
```

## Thoughts

I knew this task would be easy however I did not have enough knowledge to solve this challenge quick.

---

- https://www.root-me.org/en/Challenges/Network/FTP-authentication
