"""
Temperature Conversion

Write a program that converts between Celsius and Fahrenheit.
The input is a single temperature value with its unit symbol,
for example: 38C, 39c, 40F, 41f. There is no space between
the number and the unit.

- If the input ends with 'C' or 'c', convert it to Fahrenheit and
  output the result with an 'F' prefix.
- If the input ends with 'F' or 'f', convert it to Celsius and
  output the result with a 'C' prefix.

The result should keep two decimal places.
Use input() to read the input, and you do not need to handle
invalid formats.
"""

# temperature_conversion.py
TempStrin = input("Please input a temperature including the unit symbol (e.g. 38C, 39c, 40F, 41f)\n"
"Your input: "
)
if TempStrin[-1] in ["F","f"]:
    C = (eval(TempStrin[0:-1])-32)*5/9
    print("The converted temperature is {:.2f}℃".format(C))
elif TempStrin[-1] in ["C","c"]:
    F = eval(TempStrin[0:-1])*9/5+32
    print("The converted temperature is {:.2f}℉".format(F))
else:
    print("There is an error occured, please check the input format.")


