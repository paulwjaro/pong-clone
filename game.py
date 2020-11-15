from turtle import Turtle, Screen
from paddles import Paddle


class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=1000, height=700)
        self.running = True
        self.screen.bgcolor("black")
        self.id = None

    def screen_setup(self):
        self.id = Turtle()
        line = self.id
        line.hideturtle()
        line.width(4)
        line.penup()
        line.color("white")
        line.speed("fastest")
        line.setheading(270)
        line.goto(0, 350)
        line_up = True
        for i in range(int(700 / 20)):
            if line_up:
                line.pendown()
                line_up = False
            else:
                line.penup()
                line_up = True
            line.goto(0, line.ycor() - 20)

    def screen_close(self):
        self.screen.exitonclick()

    def init_game(self):
        self.screen_setup()
        self.paddle1 = Paddle()

