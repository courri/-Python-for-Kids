class StickFigureSprite(Sprite):
    def __init__(self, game):
        Sprite.__init__(self, game)
        self.images_left = [
            PhotoImage(file="stick-L1.gif"),
            PhotoImage(file="stick-L2.gif"),
            PhotoImage(file="stick-L3.gif")
        ]
        self.images_right = [
            PhotoImage(file="stick-R1.gif"),
            PhotoImage(file="stick-R2.gif"),
            PhotoImage(file="stick-R3.gif")
        ]
        self.image = game.canvas.create_image(200, 470, image=self.images_left[0], anchor='nw')
        self.x = -2
        self.y = 0
        self.current_image = 0
        self.current_image_add = 1
        self.jump_count = 0
        self.last_time = time.time()
        self.coordinates = Coords()
        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        game.canvas.bind_all('<space>', self.jump)
        
    def turn_left(self, evt):
        if self.y == 0:
            self.x = -2
            
    def turn_right(self, evt):
        if self.y == 0:
            self.x = 2
            
    def jump(self, evt):
        if self.y == 0:
            self.y = -4
            self.jump_count = 0
