from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(xcor, ycor)

    def move_up(self):
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.forward(20)

    def move_down(self):
        self.setheading(270)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.forward(20)
