from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super(Paddle, self).__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.move_speed = 20

    def create_paddle(self, x, y):
        self.color("white")
        self.goto(x, y)

    def move_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + self.move_speed)

    def move_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - self.move_speed)
