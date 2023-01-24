from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 250)
        self.display_score()

    def add_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def display_score(self):
        self.write(f"Current Score: {self.score}", align="center", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=('Arial', 20, 'normal'))