import random
from turtle import Screen, delay, speed
from cars import Car
from turtle_player import Player
import time
from score import Score

screen=Screen()
screen.setup(width=800,height=600)
screen.tracer(0)
color=["blue","cyan","chocolate","DarkOrchid1","green","gold","red","magenta",'salmon']
turtle_player=Player()
score=Score()
cars=[]

for i in range(8):
    car=Car()
    cars_no=[-280,-210,-140,-80,-20,40,100,160,220,280]
    car.color(random.choice(color))
    car.goto(410,cars_no[random.randint(0,9)])
    cars.append(car)
        
   
    






game_on=True
car_speed = 0  # initial car speed
car_speed_increment = 10  # increase car speed by this amount each time
max_car_speed = 50  # maximum car speed
min_time_sleep = 0.05  # minimum time sleep

#Restart game
def start_game():
    global game_on, car_speed,car_speed_increment,max_car_speed,min_time_sleep
    game_on=True
    car_speed = 0  # initial car speed
    car_speed_increment = 10  # increase car speed by this amount each time
    max_car_speed = 50  # maximum car speed
    min_time_sleep = 0.05  # minimum time sleep
    score.reset_score()
    turtle_player.goto(0, -280)
    for car in cars:
         car.goto(410, random.choice([-280,-210,-140,-80,-20,40,100,160,220,280]))

screen.onkey(key="Up",fun=turtle_player.move_player_up)
screen.onkey(key="Down",fun=turtle_player.move_player_down)
screen.listen()

while game_on:                          
    time.sleep(max(min_time_sleep, 0.15 - car_speed / 100))  # reduce sleep time for smoother animation
    for car in cars:
        # move the car forward by car_speed units
        car.move()
        if car.xcor()<-300:
            car.goto(410, random.choice(cars_no))
        if car.distance(turtle_player) < 20:  # check if turtle hits the car
            decision=screen.textinput(title="Do you Enjoy?",prompt="DO you want to play again? (yes/no)?")
            
            if decision=="yes":
                start_game()
                screen.listen()
            else:
                game_on = False
                score.game_over()
             # restart the game
            print("Game Over!")


    if turtle_player.ycor() > 280:  # check if turtle crosses the screen
        car_speed = min(car_speed + car_speed_increment, max_car_speed)  # increase car speed
        turtle_player.goto(0, -280)
        score.update_score()
        # reset turtle position
    

    screen.update()        








screen.exitonclick()