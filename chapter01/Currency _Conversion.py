'''The Chinese yuan (RMB) and the US dollar (USD) are two widely used currencies.
Write a program to convert between these two currencies. The fixed exchange rate is:
1 USD = 6.78 RMB
The program should read one line of input representing an amount in either RMB or USD, and output the converted value in the other currency.
Amounts in RMB use the prefix RMB (e.g. RMB123)
Amounts in USD use the prefix USD (e.g. USD20)
There is no space between the currency symbol and the number.
The result should keep two decimal places.
Notes:
This is an online judge problem: use input() to read the input.
You do not need to handle or report format errors.
'''

# Currency Conversion.py
TempStrin = input()
if TempStrin[0:3] == "RMB":
    USD = eval(TempStrin[3:])/6.78
    print("USD{:.2f}".format(USD))
elif TempStrin[0:3] == "USD":
    RMB = eval(TempStrin[3:])*6.78
    print("RMB{:.2f}".format(RMB)) 
else:
    print()
