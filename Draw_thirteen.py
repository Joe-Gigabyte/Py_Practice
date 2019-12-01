import os
os.system('clear')
import turtle

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Joe's Art")


my_pen = turtle.Turtle()
my_pen.speed()
i = 1
x = 2
my_pen.up()
my_pen.goto(0,0)
my_pen.down()
my_pen.speed(100)
size=1
my_pen.hideturtle()

while (i <= 200):
    for _ in range(4):
        my_pen.pensize(20)
        my_pen.color('orange')
        my_pen.circle(size,45)
        my_pen.right(5)
        my_pen.color('gold')
        my_pen.circle(size,90)
        my_pen.right(22.5)
        size = size + 1
        i += 1
while(x <= 100):
    for _ in range(4):
        my_pen.up()
        my_pen.goto(0,0)
        my_pen.down()
        my_pen.pensize(2)
        my_pen.color('black')
        my_pen.right(22.5)
        my_pen.circle(size,90)
        my_pen.right(45)
        size = size + 1
        x += 1


turtle.done()