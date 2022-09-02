from turtle import Turtle, Screen, colormode
import random as rn
from obstacles import Objects
from player import Player
from score import Score
import time

colormode(255)

screen = Screen()
screen.setup(width=600, height= 600)
screen.tracer(0)

obstacles = Objects()

player = Player()

score = Score()


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    obstacles.create_objects()
    obstacles.move()
    player.move()

    for segment in obstacles.segments:
        if player.distance(segment) < 15:
            score.game_over()
            print(segment)
            game_on = False
        if player.ycor() > 230:
            score.winner()
            game_on = False
















screen.exitonclick()