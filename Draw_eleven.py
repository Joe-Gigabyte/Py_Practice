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


while (i <= 125):
    for _ in range(5):
        my_pen.pensize(2)
        my_pen.color('red')
        my_pen.forward(size)
        my_pen.right(45)
        my_pen.color('yellow')
        my_pen.circle(size / 2, 90)



        size = size + 1


    i += 1



turtle.done()