from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.beginning_heading = 20
        self.time_factor = 0.1

    def move(self, paddle1, paddle2):
        self.setheading(self.beginning_heading)
        self.forward(20)
        if self.collision_with_wall():
            current_heading = self.heading()
            self.setheading(-current_heading)
            self.beginning_heading = self.heading()
        if self.collision_with_paddle(paddle1) or self.collision_with_paddle(paddle2):
            current_heading = self.heading()
            self.setheading(180 - current_heading)
            self.beginning_heading = self.heading()

    def collision_with_wall(self):
        if self.ycor() > 270 or self.ycor() < -270:
            return True

    def collision_with_paddle(self, paddle):
        if self.xcor() > 320 and self.distance(paddle) < 51 or self.xcor() < -330 and self.distance(paddle) < 51:
            if self.time_factor > 0:
                self.time_factor *= 0.9
            return True

    def l_out_of_bounds(self):
        if self.xcor() < -410:
            return True

    def r_out_of_bounds(self):
        if self.xcor() > 410:
            return True

    def reset_position(self):
        self.time_factor = 0.1
        self.goto(0, 0)
        current_heading = self.heading()
        self.setheading(180 - current_heading)
        self.beginning_heading = self.heading()