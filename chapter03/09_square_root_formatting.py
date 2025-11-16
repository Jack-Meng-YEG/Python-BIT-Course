"""
Square-root formatting.

Read an integer a from standard input, compute the square root of a,
and print the result rounded to 3 decimal places.

The output should be formatted in a field of width 30 characters,
right-aligned. Any unused leading positions must be filled with '+'
characters instead of spaces.

If the formatted result is longer than 30 characters, print the full
result (do not truncate).

Example:
input : 10
output: ++++++++++++++++++++++++3.162
"""

# square_root_formatting.py
a = eval(input())
b = pow(a,0.5)
print("{:+>30.3f}".format(b))
