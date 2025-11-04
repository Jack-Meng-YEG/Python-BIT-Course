# 1) Basic usage: read a string
# name = input("Please enter your name: ")
# city = input("Which city do you live in? ")

# 2) Read an integer: convert with int()
# age = int(input("Please enter your age: "))
# count = int(input("How many tickets do you want? "))

# 3) Read a float: convert with float()
# temp_c = float(input("Enter today's temperature (°C): "))
# price = float(input("Enter the price: "))

# 4) Multiline prompt using \n
# code = input("Enter a 4-digit code:\n(e.g. 1234)\nYour input: ")
# score = float(input("Enter your score:\n(e.g. 85.5)\nYour input: "))
# or
# code = input("Enter a 4-digit code:\n"
#              "(e.g. 1234)\n"
#              "Your input: "
#              )
# score = float(input("Enter your score:\n"
#                     "(e.g. 85.5)\n"
#                     "Your input: "
#                     ))

# 5) Multiline prompt using triple quotes
# message = input("""Please enter a short message:
# (press Enter when you finish)
# Your message: """)
# choice = input("""Choose an option:
# 1) Start
# 2) Quit
# Your choice: """)

# 6) Strip leading and trailing spaces
# email = input("Enter your email: ").strip()
# user_id = input("Enter your user ID: ").strip()

# 7) Read multiple items and split into a list
# words = input("Enter several words separated by spaces: ").split()
# numbers = input("Enter some numbers separated by spaces: ").split()

# 8) Read multiple integers with split() + map(int, ...)
# x, y = map(int, input("Enter two integers (e.g. 3 5): ").split())
# a, b, c = map(int, input("Enter three integers (e.g. 1 2 3): ").split())

# 9) Read a value with a unit at the end
# temp_str = input("Enter a temperature with unit (e.g. 38C, 100F): ")
# unit = temp_str[-1]
# value = float(temp_str[:-1])
