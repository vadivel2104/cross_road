from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("dark orchid")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write("Help the Turtle to cross the obstacles", align="center", font=("courier", 10, "normal"))

    def winner(self):
        self.clear()
        self.goto(0, 280)
        self.write("You Won, you helped turtle to cross the road", align="center", font=("courier", 10, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 280)
        self.write("You lost, turtle taken hit by a obstacle", align="center", font=("courier", 10, "normal"))
