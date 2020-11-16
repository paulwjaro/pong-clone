from turtle import Turtle


class GUI(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setheading(270)
        self.goto(0, 300)
        self.pensize(6)
        self.pendown()
        self.pen_position = "down"

    def create_gui(self):
        for i in range(int(600/20)):
            self.forward(20)
            if self.pen_position == "down":
                self.penup()
                self.pen_position = "up"
            else:
                self.pendown()
                self.pen_position = "down"







class Scoreboard():
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.y_pos = 200
        self.x_pos = 200
        self.score1 = Turtle()
        self.score1.penup()
        self.score1.color("white")
        self.score1.hideturtle()
        self.score1.goto(self.x_pos, self.y_pos)
        self.score2 = Turtle()
        self.score2.penup()
        self.score2.color("white")
        self.score2.hideturtle()
        self.score2.goto(-self.x_pos, self.y_pos)

    def write_score(self):
        self.score1.write(self.player1_score, False, "center", ("arial", 40, "normal"))
        self.score2.write(self.player2_score, False, "center", ("arial", 40, "normal"))

    def update_score(self, player1):
        if player1:
            self.player1_score += 1
        else:
            self.player2_score += 1
