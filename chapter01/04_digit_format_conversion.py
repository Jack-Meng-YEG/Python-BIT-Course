"""
Digit Format Conversion

Read a positive integer from the user and output the corresponding Chinese character for each digit.

The mapping for digits 0–9 is defined as follows:
0 → 零, 1 → 一, 2 → 二, 3 → 三, 4 → 四,
5 → 五, 6 → 六, 7 → 七, 8 → 八, 9 → 九

Input:
A positive integer without spaces, such as:
123
9876543210

Output:
The corresponding Chinese characters, each printed continuously (no spaces unless required).
Example:
Input: 123
Output: 一二三
"""

# digit_format_conversion.py
table = "零一二三四五六七八九"
TemStr = input()
for i in TemStr:
    print(table[eval(i)], end="")