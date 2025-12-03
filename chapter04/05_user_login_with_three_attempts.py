"""
Problem: User login with three attempts.

Write a program that gives the user up to three chances to enter a
username and a password. For each attempt, read two lines from input:
the first line is the username and the second line is the password.

- If the username is 'Kate' and the password is '666666', print a
  login-success message and terminate the program immediately.
- If, after three attempts, the username or password is still incorrect
  on every attempt, print a login-failure message and terminate the
  program.
"""

# user_login_with_three_attempts.py
count = 0
while count < 3:
    name = input()
    password = input()
    if name == 'Kate' and password == '666666':
        print("Login successful!")
        break
    else:
        count += 1
        if count == 3:
            print("Username or password incorrect in all three attempts. Exiting program.")