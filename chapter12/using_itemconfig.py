from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
mytriangle = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='red')
canvas.itemconfig(mytriangle, fill='blue')
canvas.itemconfig(mytriangle, outline='red')
