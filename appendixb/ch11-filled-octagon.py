import turtle
t = turtle.Pen()
def octagon(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1,9):
        t.forward(size)
        t.right(45)
    if filled == True:
        t.end_fill()
        
t.color(1, 0.85, 0)
octagon(40, True)
t.color(0, 0, 0)
octagon(40, False)