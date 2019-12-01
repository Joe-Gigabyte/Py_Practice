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


while (i <= 125):
    for _ in range(2):
          my_pen.color('red')
          my_pen.forward(size)
          my_pen.right(200)
          my_pen.color('orange')
          my_pen.forward(size)
          my_pen.circle(5)
          #my_pen.pencolor('blue')
          size=size + 1
    my_pen.right(10)
    #my_pen.pencolor('yellow')
    i += 1



turtle.done()