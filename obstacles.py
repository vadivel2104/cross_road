from turtle import Turtle, colormode
import random as rn




class Objects:

    def __init__(self):
        self.segments = []
        self.create_objects()
        self.y_cor = 0
        self.x_cor = 300
        self.xmove = 50
        self.r = 0
        self.g = 0
        self.b = 0
        self.new_color = (self.r, self.g, self.b)

    def create_objects(self):
        new_objects = Turtle()
        new_objects.shape("square")
        self.r = rn.randint(0, 255)
        self.g = rn.randint(0, 255)
        self.b = rn.randint(0, 255)
        self.new_color = (self.r, self.g, self.b)
        new_objects.color(self.new_color)
        new_objects.penup()
        new_objects.shapesize(stretch_wid=1, stretch_len=3)
        self.y_cor = rn.randint(-50, 200)
        self.x_cor = 300
        new_objects.goto(self.x_cor, self.y_cor)
        self.segments.append(new_objects)


    def move(self):
        # if len(self.segments) > 5:
        for segment in self.segments:
            new_x = segment.xcor() - self.xmove
            new_y = segment.ycor()
            segment.goto(new_x, new_y)














