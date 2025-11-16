"""
Caesar cipher (shift by 3)
--------------------------
Read a line of text from standard input. The string may contain
lowercase letters 'a'–'z', uppercase letters 'A'–'Z', spaces and
other symbols.

For each alphabetic character, encrypt it using a Caesar cipher with
a shift of +3 positions in the alphabet:
    - 'a' -> 'd', 'b' -> 'e', ..., 'x' -> 'a', 'y' -> 'b', 'z' -> 'c'
    - 'A' -> 'D', 'B' -> 'E', ..., 'X' -> 'A', 'Y' -> 'B', 'Z' -> 'C'
Non-alphabetic characters (spaces, punctuation, etc.) are left unchanged.

Output the encrypted string as the result.
"""

# caesar_cipher.py
temstr=input()
outstr=''
for c in temstr:
    if 'a'<= c <= 'z':
        outstr+=chr(ord('a')+(ord(c)-ord('a')+3)%26)
    elif 'A' <= c <= 'Z':
        outstr+=chr(ord('A')+(ord(c)-ord('A')+3)%26)
    else:
        outstr+=c
print(outstr)