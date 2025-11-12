"""
Problem: Cubic Formatting

Read a single number a from standard input (it may be an integer or a float).
Compute a**3 and print the result using a field width of 20 characters,
center-aligned and padded with hyphens ('-').

If the string representation of the result is longer than 20 characters,
print it as-is (do not truncate).

Input:
    One line containing a (int or float).
Output:
    The cube of a, centered in a width of 20 with '-' padding.

Example
Input:
    10
Output:
    -----1000-----
(Note: total width is 20; padding is with '-'.)
"""

# cubic_formatting.py
a=eval(input())
print("{:-^20}".format(pow(a,3)))