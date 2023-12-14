---
title: Base64
date: 2023-10-25
tags:
  - cryptography
  - encoding/base64
---

# Base64

---

## RFC 4648

> [!INFO]
> A 65-character subset of US-ASCII is used, enabling 6 bits to be represented per printable character. (The extra 65th character, "=", is used to signify a special processing function.)
>
> The encoding process represents 24-bit groups of input bits as output strings of 4 encoded characters. Proceeding from left to right, a 24-bit input group is formed by concatenating 3 8-bit input groups. These 24 bits are then treated as 4 concatenated 6-bit groups, each of which is translated into a single character in the base 64 alphabet.
>
> Each 6-bit group is used as an index into an array of 64 printable characters. The character referenced by the index is placed in the output string.

## Base64 Encoding Table

This is the Base64 alphabet defined in [RFC 4648 §4](https://datatracker.ietf.org/doc/html/rfc4648#section-4)

| Index       | Binary | Char |     | Index | Binary | Char |     | Index | Binary | Char |     | Index | Binary | Char |
| ----------- | ------ | ---- | --- | ----- | ------ | ---- | --- | ----- | ------ | ---- | --- | ----- | ------ | ---- |
| 0           | 000000 | A    |     | 16    | 010000 | Q    |     | 32    | 100000 | g    |     | 48    | 110000 | w    |
| 1           | 000001 | B    |     | 17    | 010001 | R    |     | 33    | 100001 | h    |     | 49    | 110001 | x    |
| 2           | 000010 | C    |     | 18    | 010010 | S    |     | 34    | 100010 | i    |     | 50    | 110010 | y    |
| 3           | 000011 | D    |     | 19    | 010011 | T    |     | 35    | 100011 | j    |     | 51    | 110011 | z    |
| 4           | 000100 | E    |     | 20    | 010100 | U    |     | 36    | 100100 | k    |     | 52    | 110100 | 0    |
| 5           | 000101 | F    |     | 21    | 010101 | V    |     | 37    | 100101 | l    |     | 53    | 110101 | 1    |
| 6           | 000110 | G    |     | 22    | 010110 | W    |     | 38    | 100110 | m    |     | 54    | 110110 | 2    |
| 7           | 000111 | H    |     | 23    | 010111 | X    |     | 39    | 100111 | n    |     | 55    | 110111 | 3    |
| 8           | 001000 | I    |     | 24    | 011000 | Y    |     | 40    | 101000 | o    |     | 56    | 111000 | 4    |
| 9           | 001001 | J    |     | 25    | 011001 | Z    |     | 41    | 101001 | p    |     | 57    | 111001 | 5    |
| 10          | 001010 | K    |     | 26    | 011010 | a    |     | 42    | 101010 | q    |     | 58    | 111010 | 6    |
| 11          | 001011 | L    |     | 27    | 011011 | b    |     | 43    | 101011 | r    |     | 59    | 111011 | 7    |
| 12          | 001100 | M    |     | 28    | 011100 | c    |     | 44    | 101100 | s    |     | 60    | 111100 | 8    |
| 13          | 001101 | N    |     | 29    | 011101 | d    |     | 45    | 101101 | t    |     | 61    | 111101 | 9    |
| 14          | 001110 | O    |     | 30    | 011110 | e    |     | 46    | 101110 | u    |     | 62    | 111110 | +    |
| 15          | 001111 | P    |     | 31    | 011111 | f    |     | 47    | 101111 | v    |     | 62    | 111111 | /    |
| **Padding** | =      |

---

## Implementation

```python
def encode_to_base64(padded_data: int, paddings: int = 0) -> str:
    """
    Assume that the input raw data is padded.
    """

    TABLE: str      = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    PADDING: str    = '='
    MASK: int       = (0b1 << 6) - 1

    base64_encoded: str = PADDING * paddings


    counter: int = padded_data
    sextet: int = counter & MASK
    i: int = 0
    while counter > 0:
        base64_encoded += TABLE[sextet]

        i += 1
        counter = (padded_data >> 6*i)
        sextet = counter & MASK

    return base64_encoded[::-1]


def pad_bytes(string: str) -> tuple:
    data: int       = int(string, 16)
    n_bytes: int    = (data.bit_length() + 7) // 8
    n_bits: int     = n_bytes * 8

    n = n_bits % 6
    bits_to_pad: int    = (6 - n) if n > 0 else 0
    padded_data: int    = data << bits_to_pad
    return (padded_data, bits_to_pad//2)
```

> [!INFO]
> This Python implementation could have been better if it does not require counting the bits, copying data, and reversing the string.

```rust
fn encode_from_bytes(input: &[u8]) -> String {
    let mut output: Vec<u8> = Vec::new();
    let mut temp: u32 = 0;
    let mut temp_len: u32 = 0;
    for &byte in input {
        temp = (temp << 8) | byte as u32;
        temp_len += 8;
        while temp_len >= 6 {
            temp_len -= 6;
            let chunk: u32 = temp >> temp_len;
            let char_idx: u32 = chunk & 0x3F;
            let character: u8 = CHARSET[char_idx as usize];
            output.push(character);
        }
    }
    if temp_len > 0 {
        let idx: u32 = temp << (6 - temp_len) & 0x3F;
        let character: u8 = CHARSET[idx as usize];
        output.push(character);
    }
    while output.len() % 4 != 0 {
        output.push(b'=');
    }
    String::from_utf8(output).unwrap()
}
```


> [!INFO]
> A better implementation than the python code above.