from turtle import Turtle


class Paddle:
    def __init__(self):
        self.id = Turtle(shape="square")
        paddle = self.id
        paddle.hideturtle()
        paddle.color("white")
        paddle.shapesize(4.5, 0.75)
        paddle.penup()
        paddle.setx(-460)
        paddle.showturtle()
