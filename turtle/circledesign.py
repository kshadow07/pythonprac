import turtle as t
import random

tim= t.Turtle()
tim.speed("fastest")
color=["red","blue","green","yellow","purple"]

def circledesign(gap):
    for _ in range(int(360/gap)):
        tim.color(random.choice(color))
        tim.circle(150)
        tim.setheading(tim.heading()+gap)
       
circledesign(3)        
    






screen=t.Screen()
screen.exitonclick()