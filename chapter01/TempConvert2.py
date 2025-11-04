# TempConvert2.py
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