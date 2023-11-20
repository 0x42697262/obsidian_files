---
title: (root-me.org) Twitter authentication
date: 2023-11-21
tags:
  - ctf/root-me
  - networking/security
  - packet-capture-analysis
---

# (root-me.org) Twitter authentication

---

## Details

A twitter authentication session has been captured, you have to retrieve the password.

## Solution

Open the packet in [[Wireshark]], you will see a frame with a [[HTTP]] data. The password is stored in the authorization header encoded as [[Base64]].
## Thoughts

I used linux's [[Base64]] decoding utility `base64`. I was able to acquire the username and password however I kept trying inputting the password in the validation field in root-me but I kept getting an error. What actually happened is I included the text "base64" when I copied the decoded password. That was never meant to be decoded.

I have noticed that some web servers uses the `Authorization` header for authentication with value `Basic <base64>`. It is just a thought since it is quite similar to [[(root-me.org) ETHERNET - frame|this]] ctf challenge. Although it was never implied which [[HTTP]] server was used.

---

- https://www.root-me.org/en/Challenges/Network/Twitter-authentication-101