"""
Notes:
        https://github.com/KrulYuno/obsidian_files/blob/master/Notes/020%20Studies/CMSC%20142%20Machine%20Problem%201.md
"""

import re

identifier_chars = ['_']
lower_letters = [chr(c) for c in range(97, 123)]
upper_letters = [chr(c) for c in range(65, 91)]
digits = [chr(c) for c in range(48, 58)]

for _ in digits:
        identifier_chars.append(_)
for _ in lower_letters:
        identifier_chars.append(_)
for _ in upper_letters:
        identifier_chars.append(_)

literal_chars = ['"', '\'']



class Scanner:
    def __init__(self, source: str) -> None:
        self.source = source
        self.tokens = list()

        self.start = 0
        self.current = 0
        self.line = 1
          

def main():
    # Take inputs, assume inputs are correct
    # no sanitization
    lines = int(input())
    source_code = list()
    for _ in range(lines):
        source_code.append(input())
    
    print(source_code)

if __name__ == "__main__":
    main()
