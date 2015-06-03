class Animals:
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('eating leaves')
    def left_foot_forward(self):
        print('left foot forward')
    def right_foot_forward(self):
        print('right foot forward')
    def left_foot_backward(self):
        print('left foot back')
    def right_foot_backward(self):
        print('right foot back')
    def dance(self):
        self.left_foot_forward()
        self.left_foot_backward()
        self.right_foot_forward()
        self.right_foot_backward()
        self.left_foot_backward()
        self.right_foot_backward()
        self.right_foot_forward()
        self.left_foot_forward()

reginald = Giraffes()
reginald.dance()