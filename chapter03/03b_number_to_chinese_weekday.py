"""
Prompt the user to enter a number from 1 to 7 and print the corresponding
Chinese weekday name.

Mapping:
1 → 星期一, 2 → 星期二, ..., 7 → 星期日.

If the user enters a number outside the range 1–7, print an error message
asking them to check the input.
"""

# number_to_chinese_weekday.py
day_number=eval(input("请输入星期数字（1-7）："))
week_days="星期一星期二星期三星期四星期五星期六星期日"
if 1<= day_number <=7:
    print("今天是{}。".format(week_days[day_number*3-3:(day_number-1)*3+3]))
else:
    print("请检查输入的数字，谢谢！")