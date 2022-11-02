from turtle import Turtle
PADDLE_SIZE = 5
PADDLE_SPEED = 30

class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.turtlesize(stretch_len=PADDLE_SIZE)
        self.penup()
        self.goto(xcor, ycor)

    def up(self):
        if self.ycor() < 269:
            self.forward(PADDLE_SPEED)

    def down(self):
        if -239 < self.ycor():
            self.backward(PADDLE_SPEED)
