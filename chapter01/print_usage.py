# 1) Basic usage: print a simple string
print("Hello, world!")
print("Python is fun.")

# 2) Print multiple values separated by spaces
name = "Jack"; age = 35
print("Name:", name)
print("Age:", age, "years old")

# 3) f-string formatting (recommended)
score = 89.5
print(f"Your score is {score}.")
print(f"{name} is {age} years old.")

# 4) format() formatting with placeholders
pi = 3.1415926
print("pi is {:.2f}".format(pi))
print("Temperature: {:.1f}°C".format(23.78))

# 5) Custom separator with sep=
print("A", "B", "C", sep=", ")
print("2025", "11", "04", sep="-")

# 6) Custom line ending with end=
print("Loading", end="...")
print("done")
print("Line 1", end="\n---\n"); print("Line 2")

# 7) Special characters: \n for newline, \t for tab
print("Line 1\nLine 2")
print("Name\tScore")

# 8) Raw string: prefix r"" so backslashes are not escaped
print(r"C:\Users\Jack\Desktop")
print(r"Regex pattern: \d+ means one or more digits")

# 9) Width and alignment using format()
print("{:>10}".format("hello"))   # right aligned in width 10
print("{:<10}".format("hello"))   # left aligned in width 10

# 10) Print to a file using file=
with open("log.txt", "w", encoding="utf-8") as f:
  print("Program started.", file=f)
  print("Temperature = 23.5°C", file=f)

