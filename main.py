from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
# Create Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
screen.listen()
# Create paddle1
pad1 = Paddle(-360, 0)
# Create paddle2
pad2 = Paddle(350, 0)
# Create ball
ball = Ball()
# Create score
score = Scoreboard()
# Pad movement
screen.onkeypress(pad2.up, "Up")
screen.onkeypress(pad2.down, "Down")
screen.onkeypress(pad1.up, "w")
screen.onkeypress(pad1.down, "s")
screen.onkeypress(pad1.up, "W")
screen.onkeypress(pad1.down, "S")
# Game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.time_factor)
    ball.move(pad1, pad2)
    if ball.r_out_of_bounds():
        ball.reset_position()
        score.score1 += 1
        score.refresh_score()
    if ball.l_out_of_bounds():
        ball.reset_position()
        score.score2 += 1
        score.refresh_score()
screen.exitonclick()
