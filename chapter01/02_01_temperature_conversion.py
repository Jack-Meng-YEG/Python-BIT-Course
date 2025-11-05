"""
Temperature Conversion 2

Write a program that converts between Celsius and Fahrenheit.
The input is a single temperature value with its unit symbol
at the beginning, for example: C38, c39, F40, f41.
There is no space between the unit and the number.

- If the input starts with 'C' or 'c', convert it to Fahrenheit and
  output the result with an 'F' prefix.
- If the input starts with 'F' or 'f', convert it to Celsius and
  output the result with a 'C' prefix.

The result should keep two decimal places.
Use input() to read the input.
"""

# temperature_conversion.py
TempStrin = input("Please input a temperature including the unit symbol (e.g. C38, c39, F40, f41)\n"
                  "Your input: "
                  )
if TempStrin[0] in ["F","f"]:
    C = (eval(TempStrin[1:])-32)/1.8
    print("The converted temperature is C{:.2f}" .format(C))
elif TempStrin[0] in ["C","c"]:
    F = eval(TempStrin[1:])*1.8+32
    print("The converted temperature is F{:.2f}" .format(F))
else:
    print("There is an error occured, please check the input format.")
