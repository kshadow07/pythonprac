from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.goto(0,-300)
        self.left(90)
        self.move_player_up()
        self.move_player_down()
        
    def move_player_up(self):
        self.goto(0,self.ycor()+15) 
    def move_player_down(self):
        self.goto(0,self.ycor()-15)     