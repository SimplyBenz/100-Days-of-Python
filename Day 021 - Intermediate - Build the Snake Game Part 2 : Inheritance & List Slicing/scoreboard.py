from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Menlo", 14, "normal")

class ScoreBoard(Turtle):    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,278)
        self.score = 0
        # self.color("white")
        self.Update_ScoreBoard()
        
    def Update_ScoreBoard(self):
        self.write(f"SCORE: {self.score}", move=False, align=ALIGNMENT, font=FONT)        
        
    def Increased_Score(self):
        self.score += 1
        self.clear()
        self.Update_ScoreBoard()
        
    def Game_Over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)   