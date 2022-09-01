from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color('red')
        self.shapesize(.75, .75)
        self.goto(0, -285)

    def move(self, toggle_x, toggle_y):
        if toggle_x:
            new_x = self.xcor() + 2
        else:
            new_x = self.xcor() - 2
        if toggle_y:
            new_y = self.ycor() + 2
        else:
            new_y = self.ycor() - 2
        self.goto(new_x, new_y)