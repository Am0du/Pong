from turtle import Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG')
screen.listen()

screen.tracer(0)
player1 = Paddle((350, 0))
player2 = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.onkey(player1.down, 'Down')
screen.onkey(player1.up, 'Up')

screen.onkey(player2.up, 'w')
screen.onkey(player2.down, 's')

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # Checks if the ball hits the wall
    if ball.ycor() == 300 or ball.ycor() == -300:
        ball.bounce()

    # Checks if the ball hits the paddle
    if ball.distance(player1) < 50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # checks if the ball goes out of play
    if ball.xcor() > 380:
        ball.reset_game()
        score.add_score1()

    if ball.xcor() < -380:
        ball.reset_game()
        score.add_score2()


screen.exitonclick()
