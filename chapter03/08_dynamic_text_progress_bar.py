"""
Dynamic text progress bar

Goal:
Use a text-based progress bar to show the progress of a long-running task
while updating it dynamically on a single console line.

Requirements:
1. Call time.sleep() inside a loop to simulate a task that takes time and to
   obtain a changing progress value.
2. Use print() to refresh the bar on the same line by overriding the default
   newline with end="" so that each print call does not start a new line.
3. Use '\r' (carriage return) at the beginning of the print string to move the
   cursor back to the start of the current line before drawing the next frame.

The output should show the current percentage, a bar made of '*' and '.',
and the elapsed time in seconds, with a centered "start" message at the
beginning and a centered "end" message at the end.

Note: run this script in a real command-line terminal (e.g. cmd or PowerShell
on Windows) to see the dynamic progress-bar effect; some IDE consoles ignore '\r'.
"""

# dynamic_text_progress_bar.py
import time
scale = 50
print("执行开始".center(scale//2,'-'))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale-i)
    c = i/scale*100
    t = time.perf_counter() - start
    print("\r{:3.0f}%[{}->{}]{:4.2f}s".format(c,a,b,t), end="")
    time.sleep(0.2)
print("\n"+"执行结束".center(scale//2,'-'))
