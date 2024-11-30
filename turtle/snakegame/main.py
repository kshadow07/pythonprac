from turtle import Screen
import time

from snake_logic import Snake
from food import Food
from score_board import ScoreBoard

screen=Screen()
screen.setup(width=800,height=800)
screen.bgcolor("black")
# remove the traces of the animation
screen.tracer(0)


snake=Snake()
food=Food()
score_board= ScoreBoard()


# all keyboard commands while listening to the screen
screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)


  
game_on=True
# Loop until the game_on is true
while game_on:
    
    #Update the screen every 0.1 sec so that the animation looks smooth
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect Colloison with the food and increases its length
    if snake.head.distance(food)<20:
        food.refresh()
        snake.add_new_segment()
        score_board.increase_score()
         
        
   # Detect Colloison with the wall 
    if snake.head.xcor()>390 or snake.head.xcor()<-390 or snake.head.ycor()>390 or snake.head.ycor()<-390:
        score_board.reset()
        snake.resetSnake()
        
    # Detect Colloison with the tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment)<8:
            score_board.reset()
            snake.resetSnake()
     
           
           
    

screen.exitonclick()