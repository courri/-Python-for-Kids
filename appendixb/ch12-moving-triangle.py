import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)

for x in range(0, 35):
    canvas.move(1, 10, 0)
    tk.update()
    time.sleep(0.05)

for x in range(0, 34):
    canvas.move(1, 0, 10)
    tk.update()
    time.sleep(0.05)
    
for x in range(0, 35):
    canvas.move(1, -10, 0)
    tk.update()
    time.sleep(0.05)

for x in range(0, 34):
    canvas.move(1, 0, -10)
    tk.update()
    time.sleep(0.05)