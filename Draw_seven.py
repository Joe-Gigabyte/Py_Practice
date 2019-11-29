import os
os.system('clear')
import turtle

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Joe's Art")


my_pen = turtle.Turtle()
my_pen.speed()
i = 1
my_pen.up()
my_pen.goto(0,0)
my_pen.down()
my_pen.speed(100)
my_pen.color('yellow')
size=1
size_two=3


while (i <= 75):
    for _ in range(2):
          my_pen.forward(size)
          my_pen.right(45)
          my_pen.forward(size)
          my_pen.circle(size_two)
          my_pen.pencolor('blue')
          size=size + 1
          size_two=size_two + 1
    my_pen.right(90)
    my_pen.pencolor('yellow')
    i += 1



turtle.done()