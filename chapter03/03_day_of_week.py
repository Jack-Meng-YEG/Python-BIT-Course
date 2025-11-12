"""
Ask the user to enter a number from 1 to 7 representing a day of the week,
then print the corresponding weekday name.

1 = Monday, 2 = Tuesday, ..., 7 = Sunday.
"""

# day_of_week.py
day_number=eval(input("Please enter a day of the week (1=Monday, ..., 7=Sunday):"))
week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print("The day is {}.".format(week_days[day_number-1]))
