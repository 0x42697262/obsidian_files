---
title: (root-me.org) ETHERNET - frame
date: 2023-11-20
tags:
  - "#ctf/root-me"
  - networking/security
  - packet-capture-analysis
---

# (root-me.org) ETHERNET - frame

---

## Details

Find the confidential data in a hex dump text file.

## Solution

Convert the text file as a true hex file format. I did this through Python:

```python
with open('ch12.txt') as file, open('ch12.pcap', 'wb') as fout:
	for line in file:
		fout.write(
			binascii.unhexlify(''.join(line.split()))
		)
```

Open the file as a text file then you will see `Authorization: Basic Y29uZmk6ZGVudGlhbA==`.

## Thoughts

I knew that this file cannot imported in Wireshark since it's only a frame data. I would've solved this challenge by manually decoding the frame packet however I am too lazy. Thus, I resorted to using tools to simply convert the hex strings as UTF-8 strings.

### Alternative Solutions

Add hexadecimal offsets to the hex data string. Since each line contains 16 bytes of data, the offset would be in 16.

```
000000 ...
000010 ...
000020 ...
...
0000D0 ...
```

Someone else's solution to this is to use xxd.

---

- https://www.root-me.org/en/Challenges/Network/ETHERNET-frame