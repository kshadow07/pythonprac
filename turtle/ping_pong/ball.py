from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.penup()
        self.goto(0, 0)
        self.speed("fastest")
        self.random_side=[]
        random_angle1=random.randint(135,225)
        random_angle2=random.randint(-45,45)
        self.random_side.append(random_angle1)
        self.random_side.append(random_angle2)
        self.setheading(random.choice(self.random_side))
        self.move()
        
        
    def move(self):
        self.forward(20)

            
    def direction_reverse_player1(self):
            random_angle=random.randint(-45,45)
            self.setheading(random_angle)
    
    def direction_reverse_player2(self):
            random_angle=random.randint(135,225)
            self.setheading(random_angle)                
    def upper_wall(self):
            random_angle1=random.randint(192,238)
            random_angle2=random.randint(302,348)
            if self.xcor()>0:
                self.setheading(random_angle2)
            if self.xcor()<0:
                self.setheading(random_angle1)    
           
    def lower_wall(self):
            random_angle1=random.randint(12,58)
            random_angle2=random.randint(132,178)
            if self.xcor()>0:
                self.setheading(random_angle1)
            if self.xcor()<0:
                self.setheading(random_angle2)        
                 