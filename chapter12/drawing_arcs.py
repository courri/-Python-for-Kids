from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400,height=400)
canvas.pack()

canvas.create_arc(10, 10, 200, 80, extent=45, style=ARC)
canvas.create_arc(10, 80, 200, 160, extent=90, style=ARC)
canvas.create_arc(10, 160, 200, 240, extent=135, style=ARC)
canvas.create_arc(10, 240, 200, 320, extent=180, style=ARC)
canvas.create_arc(10, 320, 200, 400, extent=359, style=ARC)
