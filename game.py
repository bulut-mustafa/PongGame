from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)
screen.listen()

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350, 0)

screen.onkey(r_paddle.up , 'Up')
screen.onkey(r_paddle.down , 'Down')
screen.onkey(l_paddle.up , 'w')
screen.onkey(l_paddle.down , 's')    

ball = Ball()
scoreboard = Scoreboard()

is_game_on = True

while(is_game_on):
    time.sleep(0.02)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.hit()
    
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.hit()
    
    if ball.xcor() > 400:
        ball.resetpos()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.resetpos()
        scoreboard.r_point()

    if scoreboard.l_score > 3 or scoreboard.r_score > 3:
        is_game_on = False
        scoreboard.goto(0,0)
        scoreboard.write('Game Over' ,align= 'center', font=('Courier', 60, 'normal'))
screen.exitonclick()