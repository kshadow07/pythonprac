
from turtle import Turtle
 



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.highScore= self.read_data()
        self.color("white")
        self.penup()
        self.goto(0,350)
        self.hideturtle()
        self.update_scoreboard()
        self.increase_score()
        self.read_data()
        self.write_data()
        
    # fetch data
    def read_data(self):
        with open('data.txt',"r") as highscore:
            score=highscore.read()
        return score 
      
    #write data        
    def write_data(self):
        with open('data.txt',"w") as highscore:
            highscore.write(str(self.highScore))
            
            
    # update the scoreBoard 
    def update_scoreboard(self):
        self.clear()
        self.write(f"Your Score is: {self.score} and High Score is: {self.highScore}", align="center", font=("Courier", 24, "normal"))
        
    
    # reset the score and update the high score
    def reset(self):
        if self.score >= int(self.highScore):
            self.highScore = self.score
            self.write_data()
            

        self.score=0
        self.read_data()
        self.update_scoreboard()
        
        
    #increase the score
    def increase_score(self):
        self.score = self.score+1
        self.update_scoreboard()
       
    
    
    # #game over function   
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
    