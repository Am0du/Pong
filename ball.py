from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.speed('slow')
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        """Moves the ball around the screen"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def bounce(self):
        """Moves the ball to the opposite direction if it hits the wall"""
        self.y_move *= -1

    def paddle_bounce(self):
        """moves the ball to the opposite direction if it hits the paddle"""
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_game(self):
        """Reset the ball when it goes out of play"""
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1
        self.ball_speed = 0.1
