from turtle import Turtle, Screen

SCREEN = Screen()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()
        self.new_y = 0

    def create_player(self):
        self.shape("turtle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def go_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)

    def move(self):
        SCREEN.listen()
        SCREEN.onkey(self.go_up, "Up")
        SCREEN.onkey(self.go_down, "Down")



