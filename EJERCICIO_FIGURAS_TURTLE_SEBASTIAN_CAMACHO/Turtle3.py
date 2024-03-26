from turtle import Turtle, Screen
import random 

colours = ["red", "blue", "yellow", "green", "orange", "black", "pink", "purple"]

Donatello = Turtle()
Donatello.shape("turtle")
Donatello.pensize(4)
Donatello.speed ("fastest")
Donatello.turtlesize (1)

for sides in range(3, 11):
    color = random.choice(colours)
    angle = 360 / sides
    Donatello.color(color)
    for _ in range(sides):
        Donatello.forward(70)
        Donatello.right(angle)

screen = Screen()
screen.exitonclick()