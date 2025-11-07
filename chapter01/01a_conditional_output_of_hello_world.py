"""
Conditional Output of 'Hello World'

Write a program that reads an integer from the user and prints "Hello World"
based on the following conditions:

1. If the input value is 0:
   → Print "Hello World" directly.

2. If the input value is greater than 0:
   → Print "Hello World" horizontally, two characters per line.
     (Note: space also counts as a character)

3. If the input value is less than 0:
   → Print "Hello World" vertically, one character per line.
"""

# conditional_output_of_hello_world.py
TemStr = input()
if eval(TemStr[:]) == 0:
    print("Hello World")
elif eval(TemStr[:]) > 0:
    print("He\nll\no \nWo\nrl\nd")
else:
    for i in "Hello World":
        print(i)