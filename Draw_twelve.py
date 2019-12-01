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
size=1
my_pen.hideturtle()

while (i <= 300):
    for _ in range(2):
        my_pen.color('yellow')
        my_pen.left(45)
        my_pen.circle(size,90)
        my_pen.color('orange')
        my_pen.left(180)
        my_pen.circle(size,90)
        my_pen.left(90)
        size = size + 1
        i += 1



turtle.done()