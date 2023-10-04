```python
"""
The algorithm goes 0 1 2 3 4 5 ... n.
Increases the each character ascii(?) per index of the string.
"""

def encrypt(text):
    encrypted_text = str()
    for i in range(len(text)):
        encrypted_text += chr(ord(text[i])+i)
    return encrypted_text

def decrypt(text):
    decrypted_text = str()
    for i in range(len(text)):
        decrypted_text += chr(ord(text[i])-i)

    return decrypted_text


if __name__ == "__main__":
    print(decrypt("d1dfg:;="))

```