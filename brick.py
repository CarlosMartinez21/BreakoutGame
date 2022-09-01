from turtle import Screen, Turtle


class Brick(Turtle):
    def __init__(self, color ,positionx, positiony):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.color(color)
        self.penup()
        self.goto(positionx, positiony)
