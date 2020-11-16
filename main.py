from turtle import Screen
from paddles import Paddle
from ball import Ball
from game import *
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
running = True
screen.tracer(0)
scoreboard = Scoreboard()
gui = GUI()
gui.create_gui()
game_speed = 0.09


def quit_game():
    global running
    running = False


player_1 = Paddle()
player_1.create_paddle(x=360, y=0)

player_2 = Paddle()
player_2.create_paddle(x=-360, y=0)

ball = Ball()
screen.onkey(key="Up", fun=player_1.move_up)
screen.onkey(key="Down", fun=player_1.move_down)
screen.onkey(key="w", fun=player_2.move_up)
screen.onkey(key="s", fun=player_2.move_down)
screen.onkey(key="q", fun=quit_game)

while running:
    screen.update()
    scoreboard.write_score()
    if ball.moving:
        ball.move_ball()
        # Detect Walls
        if ball.ycor() >= 290 or ball.ycor() <= -290:
            ball.bounce_y()

        # Detect Paddles
        if ball.xcor() >= 340 and ball.distance(player_1) <= 50:
            ball.bounce_x()
        elif ball.xcor() <= -340 and ball.distance(player_2) <= 50:
            ball.bounce_x()

        # Detect Goal
        if ball.xcor() > 400:
            ball.reset()
            ball = Ball()
            scoreboard.update_score(False)
            scoreboard.score2.clear()
        elif ball.xcor() < -400:
            ball.reset()
            ball = Ball()
            ball.x_dir = -1
            scoreboard.update_score(True)
            scoreboard.score1.clear()
    else:
        screen.onkey(key="space", fun=ball.launch_ball)
    time.sleep(ball.ball_speed)

screen.exitonclick()
