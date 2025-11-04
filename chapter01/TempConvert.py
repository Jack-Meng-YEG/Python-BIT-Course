# TempConvert.py
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