from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.player1 = 0
        self.player2 = 0
        self.update()
        self.line()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player1, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.player2, align='center', font=('Courier', 80, 'normal'))

    def add_score1(self):
        """Adds 1 to player1"""
        self.player1 += 1
        self.update()

    def add_score2(self):
        """Adds 1 to player2"""
        self.player2 += 1
        self.update()

    def line(self):
        """Draws a line to divide the table"""
        line = []
        y_cor = 300
        for _ in range(20):
            turtle = Turtle('square')
            turtle.color('white')
            turtle.turtlesize(stretch_len=0.2, stretch_wid=1)
            turtle.penup()
            turtle.goto(0, y_cor)
            line.append(turtle)
            y_cor -= 40
