from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        """Moves the paddles up"""
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def down(self):
        """Moves the paddles down"""
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)