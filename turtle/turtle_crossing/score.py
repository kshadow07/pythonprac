from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Level: {self.score}", align="center", font=("Arial"))
     
     # update the score   
    def update_score(self):
        self.clear()
        self.score+=1
        self.write(f"Level: {self.score}", align="center", font=("Arial"))
    
    #game over function   
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=("Courier", 24, "normal"))
        
    def reset_score(self):
        self.clear()
        self.goto(0,270)
        self.write(f"Level: {self.score}", align="center", font=("Arial"))
        