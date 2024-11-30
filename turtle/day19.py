from turtle import Turtle,Screen
import random
import turtle




screen=Screen()

        
    
  
race_on=False    
screen.setup(width=500,height=400)
color=["red",'blue','green','orange','purple','yellow']
y_coordinate=[-80,-40,0,40,80,120]
new_turtle=[]



bet=screen.textinput(title='make a bet',prompt="Guess the color of turtle that will win?")
for i in range(6):
    tur=Turtle(shape="turtle")
    tur.color(color[i])
    tur.penup()
    tur.goto(x=-230,y=y_coordinate[i])
    new_turtle.append(tur)


if bet:
    race_on=True

while race_on:
    for turtle in new_turtle:
        turtle.speed("fastest")
        if turtle.xcor()>230:
            winningcolor=turtle.pencolor()
            if winningcolor==bet:
                print(f"You won! The {winningcolor} turtle is the winner")
            else:
                print(f"You lost! The {winningcolor} turtle is the winner")
            race_on=False
        randistance= random.randint(0,5)
        turtle.forward(randistance)
            
    
    
    

    
        
    


screen.exitonclick()



            