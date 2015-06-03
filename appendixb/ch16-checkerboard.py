from tkinter import *
import random
import time
        
class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Game")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        
        self.canvas = Canvas(self.tk, width=500, height=500, bd=0, highlightthickness=0)
        self.canvas.pack()
        
        self.tk.update()
        
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.bg = PhotoImage(file="background.gif")
        w = self.bg.width()
        h = self.bg.height()

        draw_background = 0
        for x in range(0, 5):
            for y in range(0, 5):
                if draw_background == 1:
                    self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')
                    draw_background = 0
                else:
                    draw_background = 1
        
        self.sprites = []
        self.running = True
                
    def add(self, sprite):
        self.sprites.append(sprite)
        
    def mainloop(self):
        while 1:
            for sprite in self.sprites:
                sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)


g = Game()
g.mainloop()