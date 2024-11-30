from turtle import Screen
from player1 import Player1
from player2 import Player2
from ball import Ball
import time


screen=Screen()
screen.setup(height=850,width=900)
screen.bgcolor("pink")
screen.tracer(0)
player1=Player1()
player2=Player2()
ball=Ball()

screen.listen()
screen.onkey(key="w",fun=player1.up)
screen.onkey(key="s",fun=player1.down)
screen.onkey(key="Up",fun=player2.up)
screen.onkey(key="Down",fun=player2.down)

game_on=True
while game_on:
    screen.update()
    time.sleep(0.09)
    ball.move()
    if ball.distance(player1)<50:
        ball.direction_reverse_player1()
        ball.move()
    if ball.distance(player2)<50:
        ball.direction_reverse_player2()
        ball.move()
    if ball.ycor()>415:
        ball.upper_wall()
        ball.move()
    if ball.ycor()<-415:
        ball.lower_wall()
        ball.move()         
    if ball.xcor()>440 or ball.xcor()<-440:
        game_on= False
    


screen.exitonclick()    