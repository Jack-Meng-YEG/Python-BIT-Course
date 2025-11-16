"""
Text-based progress bar demo.

This script simulates the execution of a task by printing a simple text
progress bar.

The program:
1. Sets the total scale (number of steps) to 10.
2. Prints a "start" message.
3. Loops from 0 to scale (inclusive). For each step i:
   - Uses i '*' characters to represent the completed part.
   - Uses (scale - i) '.' characters to represent the remaining part.
   - Computes the current completion percentage as (i / scale) * 100.
   - Prints a line like: " 30%[***->.......]".
   - Pauses for 1 second so the progress appears to move over time.
4. Prints an "end" message after the loop finishes.

Example output:
------执行开始------
  0%[->..........]
 10%[*->.........]
 20%[**->........]
 30%[***->.......]
 40%[****->......]
 50%[*****->.....]
 60%[******->....]
 70%[*******->...]
 80%[********->..]
 90%[*********->.]
100%[**********->]
------执行结束------
"""

# text_based_progress_bar_demo.py
import time
scale=10
print("------执行开始------")
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    time.sleep(1)
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
time.sleep(1)
print("------执行结束------")