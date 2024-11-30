import turtle

import pandas
data=pandas.read_csv("/Python/csv/day-25-us-states-game-start/50_states.csv")
state_list=data.state

screen=turtle.Screen()
image="csv/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


chance=0
correct_answer=0

while chance<len(state_list):
    answer=screen.textinput(title="Guess the States",prompt=f"No of attempt you have{chance}/50 \n You have guessed {correct_answer} correct").title()
    chance+=1
    if answer=="Exit":
        break
    if answer in state_list.to_list():
        correct_answer+=1
        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data=data[data.state==answer]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer.capitalize())
        



   
