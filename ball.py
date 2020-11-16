from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed = 10
        self.x_dir = 1
        self.y_dir = 1
        self.moving = False
        self.ball_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_dir * self.move_speed
        new_y = self.ycor() + self.y_dir * self.move_speed

        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_dir = self.x_dir * -1
        self.ball_speed *= 0.9

    def bounce_y(self):
        self.y_dir = self.y_dir * -1

    def launch_ball(self):
        self.moving = True
