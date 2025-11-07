"""
Digit Format Conversion

Read a positive integer from the user and output the English word of each digit.

The English words for digits 0–9 are:
0 → zero, 1 → one, 2 → two, 3 → three, 4 → four,
5 → five, 6 → six, 7 → seven, 8 → eight, 9 → nine.

Input:  a positive integer (e.g. 123, 9876543210)
Output: the corresponding English words, separated by spaces.
"""

# digit_format_conversion.py
table = ["zero","one","two","three","four","five","six","seven","eight","nine"]
DigStr = input()
for i in DigStr:
    print(table[eval(i)], end=" ")