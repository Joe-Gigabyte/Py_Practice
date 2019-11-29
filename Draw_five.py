import os
os.system('clear')

import turtle

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Joe's Art")

my_pen = turtle.Turtle()
my_pen.speed(100)
i = 1

while(i <= 72):
    my_pen.up()
    my_pen.goto(0,0)
    my_pen.down()
    my_pen.color('red')
    my_pen.forward(100)
    my_pen.color('orange')
    my_pen.forward(75)
    my_pen.color('yellow')
    my_pen.right(90)
    my_pen.forward(50)
    my_pen.color('light green')
    my_pen.right(135)
    my_pen.forward(50)
    my_pen.color('light blue')
    my_pen.right(45)
    my_pen.forward(50)
    my_pen.color('indigo')
    my_pen.right(45)
    my_pen.forward(50)
    my_pen.right(90)
    my_pen.forward(50)
    my_pen.color('violet')
    my_pen.circle(5)
    my_pen.color('red')
    my_pen.right(45)
    my_pen.forward(50)
    my_pen.right(45)
    my_pen.forward(50)
    my_pen.right(-10)
    my_pen.forward(50)
    my_pen.right(45)
    my_pen.forward(50)
    my_pen.right(45)
    my_pen.forward(50)
    my_pen.right(45)
    my_pen.color('violet')
    my_pen.forward(50)
    my_pen.right(45)
    i += 1



turtle.done()