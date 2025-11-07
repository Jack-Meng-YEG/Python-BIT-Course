"""
Basic Arithmetic Evaluation

Read one line of input containing a simple arithmetic expression in the form:

    M OP N

where M and N are numbers, and OP is one of the four operators: +, -, *, /.

There may be one or more spaces between M and OP, and between OP and N.
You do not need to handle invalid input.

Compute the value of the expression and print the result, keeping exactly
two digits after the decimal point.
"""

# basic_arithmetic_evaluation.py
print("{:.2f}" .format(eval(input())))
